# IMPORT PROJET
from programs.download import Download, Scan

scan = Scan("my-hero-academia", 190, 307)
MHA = Download("MHA", scan)

MHA.process()
