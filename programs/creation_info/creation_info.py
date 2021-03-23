class CreationInfo:
    """Définition la classe CreationInfo"""

    def __init__(self):
        """
        initialiseur de la classe CreationInfo.
        """
        self._web = None
        self._name = None
        self._save = None

    # WEB
    def get_web(self):
        """Permet de récupérer web."""
        return self._web

    def set_web(self, web_path):
        """Permet de fixer la valeur de web à web_path"""
        self._web = web_path

    # NAME
    def get_name(self):
        """Permet de récupérer name."""
        return self._name

    def set_name(self, file_name):
        """Permet de fixer la valeur de name à file_name"""
        self._name = file_name

    # SAVE
    def get_save(self):
        """Permet de récupérer save."""
        return self._save

    def set_save(self, save_path):
        """Permet de fixer la valeur de save à save_path"""
        self._save = save_path
