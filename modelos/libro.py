class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Requisito: Título y autor almacenados como una tupla inmutable
        self._info_basica = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn

    # Uso de getters (encapsulamiento) para proteger los datos
    @property
    def titulo(self):
        return self._info_basica[0]

    @property
    def autor(self):
        return self._info_basica[1]

    @property
    def categoria(self):
        return self._categoria

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return (
            f"-----------------------------------\n"
            f"Título    : {self.titulo}\n"
            f"Autor     : {self.autor}\n"
            f"Categoría : {self.categoria}\n"
            f"ISBN      : {self.isbn}\n"
            f"-----------------------------------"
        )