# IMPORT SYSTEME
import os
from os import sep

import img2pdf

# IMPORT PROJET
from programs.creation_info.creation_info import CreationInfo

''' PDF '''


def generate_pdf(creation_info, nb_pages):
    """
    Permet de générer un fichier pdf à partir des différentes planches du chapitre.

    :param creation_info: (CreationInfo) les informations nécessaires à la création.
    :param nb_pages: (int) le nombre de page du pdf.
    """
    if not isinstance(creation_info, CreationInfo):
        raise TypeError("Ne peut créer un PDF qu'à l'aide d'un CreationInfo.")

    with open(creation_info.get_save() + creation_info.get_pdf_name(), "wb") as f:
        try:
            f.write(img2pdf.convert(
                [os.path.join(f"{creation_info.get_save()}", i)
                 for i in os.listdir(f"{creation_info.get_save()}")
                 if i.endswith(".jpg") and int(i.split(".")[0]) < nb_pages - 1]))
        except IndexError:
            raise IndexError("Le numéro du (premier || dernier) chapitre est supérieur "
                             "au nombre de chapitres existants.")


def suppr_img(repertory):
    """
    Permet de supprimer toutes les images .jpg d'un répertoire.

    :param repertory: le répertoire contenant les images.
    """
    for i in os.listdir(f"{repertory}"):
        if i.endswith(".jpg"):
            os.remove(repertory + i)


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


def create_repository(repository_1="", repository_2=""):
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


def save_path(repository):
    """
    Crée le chemin de sauvegarde des scans.

    :param repository: (str) le répertoire du scan.
    """
    return repository + sep


def image_name(format_id):
    """
    Crée le nom de l'image de sortie.

    :param format_id: (str) le numéro de la planche du chapitre.
    """
    return format_id + ".jpg"


def pdf_name(format_id):
    """
    Crée le nom du pdf de sortie.

    :param format_id: (str) le numéro du chapitre.
    """
    return format_id + ".pdf"
