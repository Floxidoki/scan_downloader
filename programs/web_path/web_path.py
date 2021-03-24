class WebPath:
    """Définition la classe WebPath"""

    def __init__(self, manga_name):
        """
        initialiseur de la classe WebPath.

        :param manga_name: (str) le nom du manga.
        """
        self._manga_name = manga_name
        self._link = self.generate_link()

    def generate_link(self):
        """Permet de générer le lien source."""
        return "Méthode implémentée par les classes filles."

    def get_link(self):
        """Permet de récupérer le lien source."""
        return self._link


class LelScans(WebPath):
    """Définition la classe WebPath"""

    def generate_link(self):
        """Permet de générer le lien source."""
        return "https://lelscans.net/mangas/" + self._manga_name
