class CreationInfo:
    """Définition la classe CreationInfo"""

    def __init__(self):
        """
        initialiseur de la classe CreationInfo.
        """
        self._web = None
        self._image_name = None
        self._pdf_name = None
        self._save = None

    # WEB
    def get_web(self):
        """Permet de récupérer web."""
        return self._web

    def set_web(self, web_path):
        """Permet de fixer la valeur de web à web_path"""
        self._web = web_path

    # IMAGE NAME
    def get_image_name(self):
        """Permet de récupérer image_name."""
        return self._image_name

    def set_image_name(self, name):
        """Permet de fixer la valeur de image_name à name"""
        self._image_name = name

    # PDF NAME
    def get_pdf_name(self):
        """Permet de récupérer pdf_name."""
        return self._pdf_name

    def set_pdf_name(self, name):
        """Permet de fixer la valeur de pdf_name à name"""
        self._pdf_name = name

    # SAVE
    def get_save(self):
        """Permet de récupérer save."""
        return self._save

    def set_save(self, save_path):
        """Permet de fixer la valeur de save à save_path"""
        self._save = save_path

    def __str__(self):
        print("web: " + self._web + "\n" +
              "image_name: " + self._image_name + "\n" +
              "_pdf_name: " + self._pdf_name + "\n" +
              "_save: " + self._save + "\n")
