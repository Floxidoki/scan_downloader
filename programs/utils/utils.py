# IMPORT SYSTEME
import os
from os import sep

''' CALCUL '''


def format_num(num):
    """
    Permet de formater un nombre.

    :param num: (str) le nombre à reformater

    :return: (str) le nombre après reformatation
    """
    if len(num) < 2:
        return "0" + num
    return num


''' PATH '''


def create_repository(repository_1, repository_2):
    """
    Permet de créer un répertoire.

    :param repository_1: (str) le répertoire à créer.
    :param repository_2: (str) le sous répertoire à créer.
    """
    os.system("mkdir " + repository_1 + sep + repository_2)


def web_path(manga_name, chap_id, format_id):
    """
    Recrée l'adresse https de la planche du scan.

    :param manga_name: (str) le nom du manga.
    :param chap_id: (str) le chapitre à télécharger.
    :param format_id: (str) le numéro de la planche du chapitre.

    :return: (str) l'adresse http de l'image
    """
    return "https://lelscans.net/mangas/" + manga_name + "/" + chap_id + "/" + format_id + ".jpg"


def save_path(repository, chap_id):
    """
    Crée le chemin de sauvegarde des scans.

    :param repository: (str) le répertoire du scan.
    :param chap_id: (str) le chapitre à télécharger.
    """
    return repository + sep + chap_id + sep


def file_name(format_id):
    """
    Crée le nom du fichier de sortie.

    :param format_id: (str) le numéro de la planche du chapitre.
    """
    return format_id + ".jpg"
