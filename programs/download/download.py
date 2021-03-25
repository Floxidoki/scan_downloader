# IMPORT SYSTEME
import os
import shutil

import requests

# IMPORT PROJET
from programs import utils as ul
from programs.scan.scan import Scan
from programs.creation_info.creation_info import CreationInfo


class Download:
    """Définition de la classe Download."""

    def __init__(self, repository, scan, web_path):
        """
        Initialiseur de la classe Download.

        :param repository: (str) le nom du répertoir de sauvegarde.
        :param scan: (str) le scan à télécharger.
        :param web_path: (WebPath) la base du lien de téléchargement.
        """
        if isinstance(scan, Scan):
            self._scan = scan
        else:
            raise TypeError("Ne peut télécharger que des scans.")

        self._repository = repository
        self._web_path = web_path
        self._convention = 0
        self._creationInfo = CreationInfo()
        self._current_chap = self._scan.get_deb()

    def launch_process(self):
        """
        Processus de téléchargement des chapitres.
        """
        self._init_rep()

        for chap_id in range(self._scan.get_deb(), self._scan.get_end() + 1):
            # Vérifie comment sont formater les liens du chapitre
            self._convention_test(str(chap_id))

            exist, page_id = self._init_chap(chap_id)

            while exist:
                self._init_info(chap_id, page_id)
                exist = self._download()
                page_id += 1

            self._generate_pdf(chap_id)
            print(str(self._progress()) + "%")

    def _convention_test(self, chap_id):
        """
        Permet de connaitre la convention de nommage de ce chapitre.
        """
        link = self._web_path + "/" + chap_id + "/1.jpg"
        img_data = requests.get(link, allow_redirects=True)
        if self._img_exist(img_data):
            self._convention = 1

    def _init_rep(self):
        """
        Initialise le répertoire de destination.
        """
        if os.path.exists(self._repository):
            shutil.rmtree(self._repository)

        ul.create_repository(self._repository)

    def _init_chap(self, chap):
        """
        Initialise les variables relatives au chapitre à leur valeurs de départ.

        :param chap: (str) le numéro du chapitre.
        """
        self._current_chap = chap
        if self._convention == 0:
            return True, 0
        return True, 1

    def _init_info(self, chap_id, page_id):
        """
        Initialise les informations de création.

        :param chap_id: (str) le numéro du chapitre.
        :param page_id: (str) le numéro de la page.
        """
        format_id = ul.format_num(str(page_id), self._convention)

        self._creationInfo.set_web(ul.web_path(self._web_path, str(chap_id), str(format_id)))
        self._creationInfo.set_image_name(ul.image_name(str(format_id)))
        self._creationInfo.set_save(ul.save_path(self._repository))

    def _generate_pdf(self, chap_id):
        """
        Génère le pdf pour un chapitre.

        :param chap_id: (str) le numéro du chapitre.
        """
        self._creationInfo.set_pdf_name(ul.pdf_name(str(chap_id)))
        ul.generate_pdf(self._creationInfo)

    def _download(self):
        """
        Récupérer une page depuis son adresse https et l'enregistre.

        :return: (bool) True si la planche existe sinon False.
        """
        img_data = requests.get(self._creationInfo.get_web(), allow_redirects=True)

        if self._img_exist(img_data):
            self._save_img(img_data)
            return True
        return False

    def _save_img(self, img_data):
        """
        Eenregistrer une image.

        :param img_data: (Response) l'image à sauvergarder.
        """
        open(self._creationInfo.get_save() + self._creationInfo.get_image_name(), 'wb').write(img_data.content)

    def _img_exist(self, img_data):
        """
        Permet de savoir si l'image existe.

        :param img_data: (Response) l'image à vérifier.
        """
        return img_data.__str__() != "<Response [404]>"

    def _progress(self):
        """
        Calcule la progression du téléchargement.

        :return: pourcentage: (float) le pourcentage de progression
        """
        return round(
            (((self._current_chap + 1) - self._scan.get_deb()) / ((self._scan.get_end() - self._scan.get_deb()) + 1)) *
            100, 2)

    def __str__(self):
        """
        Représentation du download.
        """
        return str(self._progress())
