# IMPORT SYSTEME
import os
import shutil

import requests
import img2pdf

# IMPORT PROJET
from programs import utils as ul
from programs.scan.scan import Scan
from programs.creation_info.creation_info import CreationInfo


class Download:
    """Définition la classe Download"""

    def __init__(self, repository, scan):
        """
        Initialiseur de la classe Download.

        :param repository: (str) le nom du répertoir de sauvegarde.
        :param scan: (str) le scan à télécharger.
        """
        self._repository = repository

        if isinstance(scan, Scan):
            self._scan = scan
        else:
            raise TypeError("Ne peut télécharger que des scans.")

        self._creationInfo = CreationInfo()

        self._current_chap = self._scan.get_deb()

    def process(self):
        """
        Permet de gérer le téléchargement du scan.
        """

        # Crée le répertoire où le chapitre sera téléchargé
        if os.path.exists(self._repository):
            shutil.rmtree(self._repository)

        ul.create_repository(self._repository)

        for chap_id in range(self._scan.get_deb(), self._scan.get_end() + 1):

            self._current_chap = chap_id
            exist = True
            page_id = 0

            # Tant que la page du chapitre existe, la télécharge dans le répertoire
            while exist:
                format_id = ul.format_num(str(page_id))

                self._creationInfo.set_web(ul.web_path(self._scan.get_manga_name(), str(chap_id), str(format_id)))
                self._creationInfo.set_image_name(ul.image_name(str(format_id)))
                self._creationInfo.set_save(ul.save_path(self._repository))

                exist = self.download()
                page_id += 1

            self._creationInfo.set_pdf_name(ul.pdf_name(str(chap_id)))
            ul.generate_pdf(self._creationInfo, page_id)

            # Calcul la progression du téléchargement
            print(str(self.progress()) + "%")

        ul.suppr_img(self._creationInfo.get_save())

    def download(self):
        """
        Permet de récupérer une planche d'un scan depuis son adresse https et de l'enregistrer.

        :return: (bool) True si la planche existe sinon False.
        """
        # Récupère l'image depuis son adresse https
        img_data = requests.get(self._creationInfo.get_web(), allow_redirects=True)

        # Si elle existe, l'ajoute dans le répertoire prévu
        if self.img_exist(img_data):
            self.save_img(img_data)
            return True
        return False

    def save_img(self, img_data):
        """
        Permet d'enregistrer une image avec le chemin et le nom voulu.

        :param img_data: (Response) l'image à sauvergarder.
        """
        open(self._creationInfo.get_save() + self._creationInfo.get_image_name(), 'wb').write(img_data.content)

    def img_exist(self, img_data):
        """
        Permet de savoir si l'image renvoie un erreur 404 (n'existe pas).

        :param img_data: (Response) l'image à vérifier.
        """
        return img_data.__str__() != "<Response [404]>"

    def progress(self):
        """
        Permet de calculer la progression du téléchargement.

        :return: pourcentage: (float) le pourcentage de progression
        """
        return round(
            (((self._current_chap + 1) - self._scan.get_deb()) / ((self._scan.get_end() - self._scan.get_deb()) + 1)) *
            100, 2)

    def __str__(self):
        """
        Permet de représenter la progression du téléchargement.
        """
        str(self.progress())
