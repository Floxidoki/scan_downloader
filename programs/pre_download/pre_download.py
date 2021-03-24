# IMPORT SYSTEME
import json

# IMPORT PROJET
from programs.download import Download, Scan
from programs.web_path.web_path import *


class PreDownload:
    """Définition la classe PreDownload"""

    def __init__(self, repository, scan):
        """
        initialiseur de la classe PreDownload.

        :param repository: (str) le nom du répertoir de sauvegarde.
        :param scan: (str) le scan à télécharger.
        """
        if isinstance(scan, Scan):
            self._scan = scan
        else:
            raise TypeError("Ne peut télécharger que des scans.")

        self._path_to_json = "scan_downloader/resources/manga.json"
        self._repository = repository

        self._sites = {
            "Lelscans": LelScans
        }

        self._pre_download()

    def _pre_download(self):
        """
        Permet de preparer le téléchargement.
        """
        with open(self._path_to_json) as json_file:
            values = json.load(json_file)

            deb = self._scan.get_deb()
            end = self._scan.get_end()
            lib_deb = values[self._scan.get_manga_name()]["deb"]
            lib_end = values[self._scan.get_manga_name()]["end"]

            if self._verify_limit(deb, end, lib_deb, lib_end):
                site = values[self._scan.get_manga_name()]["site"]
                id = values[self._scan.get_manga_name()]["id"]
                Download(self._repository, self._scan, self._sites[site](id).get_link()).launch_process()

    def _verify_limit(self, deb, end, lib_deb, lib_end):
        """
        Vérifie si les chapitres demandés sont disponibles.

        :param deb: (int) le n° du premier chapitre à télécharger.
        :param end: (int) le n° du dernier chapitre à télécharger.
        :param lib_deb: (int) le n° du premier chapitre disponible.
        :param lib_end: (int) le n° du dernier chapitre disponible.

        :return: (bool) True si disponible sinon False.
        """
        if deb <= 0:
            print("Le numéro du premier scan doit être supérieur à 0.\n" +
                  "Pour ce manga, nous n'avons les chapitres qu'à partir du n°" + str(lib_deb) + ", " +
                  "et jusqu'au n°" + str(lib_end) + ".")
            return False

        elif deb > end:
            print("Le numéro du premier scan doit être inférieur à celui du dernier.\n" +
                  "Pour ce manga, nous n'avons les chapitres qu'à partir du n°" + str(lib_deb) + ", " +
                  "et jusqu'au n°" + str(lib_end) + ".")
            return False

        elif (deb < lib_deb or deb > lib_end) and end > lib_end:
            print("Pour ce manga, nous n'avons les chapitres qu'à partir du n°" + str(lib_deb) + ", " +
                  "et jusqu'au n°" + str(lib_end) + ".")
            return False

        elif deb < lib_deb:
            print("Pour ce manga, nous n'avons les chapitres qu'à partir du n°" + str(lib_deb) + ".")
            return False

        elif end > lib_end:
            print("Pour ce manga, nous n'avons les chapitres que jusqu'au n°: " + str(lib_end) + ".")
            return False
        return True
