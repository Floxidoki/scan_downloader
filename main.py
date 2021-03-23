# IMPORT PROJET
import sys

from programs.download import Download, Scan

scan = Scan("my-hero-academia", 190, 195)
MHA = Download("MHA", scan)

MHA.process()


