# IMPORT PROJET
import sys

from programs.download import Download, Scan

if len(sys.argv) == 5:

    scan = Scan(str(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    download = Download(str(sys.argv[1]), scan)
    download.launch_process()
else:
    print("Vous devez rentrer 4 arguments:"
          "\n- Le nom du sous dossier qui recevra les scans"
          "\n- Le nom du manga, \"my-hero-academia\" par exemple"
          "\n- Le numéro du chapitre où commencer le téléchargement"
          "\n- Le numéro du chapitre où finir le téléchargement")
