# IMPORT SYSTEME
import requests
import os


def format_num(num):
    """
    Permet de formater un nombre.

    :param num: (str) le nombre à reformater

    :return: (str) le nombre après reformatation
    """
    if len(num) < 2:
        return "0" + num
    return num


def progress(deb, end, current):
    """
    Permet de calculer la progression du téléchargement.

    :param deb: (int) le chapitre où commencer le téléchargement
    :param end: (int) le chapitre où finir le téléchargement
    :param current: (int) le chapitre courrant

    :return: pourcentage: (float) le pourcentage de progression
    """
    print(round(((current - deb) / (end - deb)) * 100, 2))


def img_download(web_path, file_name, save_path):
    """
    :param web_path: adresse https de l'image.
    :param file_name: le nom sous lequel enregistrer l'image.
    :param save_path: le path de sauvegarde de l'image.

    :return: web_path: (str) l'adresse https de l'image à récupérer.
    :return: save_path: (str) le chemin où sauvegarder l'image.
    """
    # Récupère l'image depuis son adresse https
    img_data = requests.get(web_path, allow_redirects=True)

    # Si elle existe, l'ajoute dans le répertoire prévu
    if img_exist(img_data):
        img_save(img_data, save_path, file_name)
        return True
    return False


def img_save(img_data, save_path, file_name):
    """
    :param img_data: (Response) l'image à sauvergarder.
    :param save_path: (str) le chemin où sauvegarder l'image.
    :param file_name: (str) le nom de l'image.
    """
    open(save_path + file_name, 'wb').write(img_data.content)


def img_exist(img_data):
    """
    :param img_data: (Response) l'image à vérifier.
    """
    return img_data.__str__() != "<Response [404]>"
