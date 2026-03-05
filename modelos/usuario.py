class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario
        # Requisito: Utilizar lista para almacenar los libros prestados
        self._libros_prestados = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def libros_prestados(self):
        return self._libros_prestados

    def agregar_libro(self, libro):
        """Añade un libro a la lista personal del usuario."""
        self._libros_prestados.append(libro)

    def quitar_libro(self, isbn):
        """Retira el libro de la lista usando el ISBN."""
        for libro in self._libros_prestados:
            if libro.isbn == isbn:
                self._libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return (
            f"-----------------------------------\n"
            f"Usuario          : {self.nombre}\n"
            f"ID               : {self.id_usuario}\n"
            f"Libros prestados : {len(self._libros_prestados)}\n"
            f"-----------------------------------"
        )