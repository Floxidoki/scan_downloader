class Scan:
    """Définition la classe Scan"""

    def __init__(self, manga_name, deb, end):
        """
        initialiseur de la classe Scan.

        :param manga_name: (str) le nom du manga.
        :param deb: (str) le scan où commencer le téléchargement.
        :param end: (str) le scan où finir le téléchargement.
        """
        self._manga_name = manga_name

        if deb <= 0:
            raise ValueError("Le numéro du premier scan doit être supérieur à 0.")

        if deb > end:
            raise ValueError("Le numéro du premier scan doit être inférieur à celui du dernier.")

        self._deb = deb
        self._end = end

    def get_manga_name(self):
        """Permet de récupérer manga_name."""
        return self._manga_name

    def get_deb(self):
        """Permet de récupérer deb."""
        return self._deb

    def get_end(self):
        """Permet de récupérer end."""
        return self._end
