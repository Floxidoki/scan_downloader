# IMPORT PROJET
from scan_downloader import utils as ul


def download_scan(manga_name, deb, end):
    """
    :param manga_name: le nom du manga à télécharger.
    :param deb: le numéro du chapitre où commencer le téléchargement.
    :param end: le numéro du chapitre où finir le téléchargement.

    :return: web_path: l'adresse https de l'image à récupérer.
    :return: save_path: le chemin où sauvegarder l'image.
    """
    for chapitre_id in range(deb, end + 1):

        # Crée le répertoire où le chapitre sera téléchargé
        ul.create_repository("", chapitre_id)

        exist = True
        page_id = 0

        # Tant que la page du chapitre existe, la télécharge dans le répertoire
        while exist:
            format_id = ul.format_num(page_id)
            exist = ul.img_download(ul.path(manga_name, chapitre_id, format_id))
            page_id += 1

        # Calcul la progression du téléchargement
        ul.progress(deb, end, chapitre_id)
