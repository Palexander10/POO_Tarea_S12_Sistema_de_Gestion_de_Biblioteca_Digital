from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    def __init__(self):
        # Requisito: Diccionario para almacenar libros disponibles (Clave: ISBN, Valor: Objeto Libro)
        self._libros_disponibles = {}
        # Requisito: Conjunto (set) para gestionar IDs únicos de usuarios
        self._ids_usuarios = set()
        # Diccionario auxiliar para acceder a los objetos Usuario rápidamente por su ID
        self._usuarios = {}

    # --- Gestión de Libros ---
    def anadir_libro(self, libro):
        if libro.isbn in self._libros_disponibles:
            print(f"[Error] El libro con ISBN {libro.isbn} ya existe.")
        else:
            self._libros_disponibles[libro.isbn] = libro
            print(f"[Éxito] Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self._libros_disponibles:
            libro = self._libros_disponibles.pop(isbn)
            print(f"[Éxito] Libro '{libro.titulo}' retirado del catálogo.")
        else:
            print(f"[Error] No se encontró un libro con el ISBN {isbn}.")

    # --- Gestión de Usuarios ---
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self._ids_usuarios:
            print(f"[Error] El ID de usuario {usuario.id_usuario} ya está en uso.")
        else:
            self._ids_usuarios.add(usuario.id_usuario)
            self._usuarios[usuario.id_usuario] = usuario
            print(f"[Éxito] Usuario '{usuario.nombre}' registrado correctamente.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self._ids_usuarios:
            usuario = self._usuarios[id_usuario]
            if len(usuario.libros_prestados) > 0:
                print(f"[Error] {usuario.nombre} debe devolver todos sus libros antes de darse de baja.")
                return
            self._ids_usuarios.remove(id_usuario)
            del self._usuarios[id_usuario]
            print(f"[Éxito] Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"[Error] Usuario no encontrado.")

    # --- Préstamos y Devoluciones ---
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self._usuarios:
            print("[Error] El usuario no está registrado.")
            return
        if isbn not in self._libros_disponibles:
            print("[Error] El libro no está disponible o no existe en el catálogo.")
            return
        
        # Lógica de préstamo: sacarlo de disponibles y pasarlo al usuario
        usuario = self._usuarios[id_usuario]
        libro = self._libros_disponibles.pop(isbn)
        usuario.agregar_libro(libro)
        print(f"[Éxito] Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self._usuarios:
            print("[Error] El usuario no está registrado.")
            return
        
        usuario = self._usuarios[id_usuario]
        libro_devuelto = usuario.quitar_libro(isbn)
        
        if libro_devuelto:
            self._libros_disponibles[libro_devuelto.isbn] = libro_devuelto
            print(f"[Éxito] Libro '{libro_devuelto.titulo}' devuelto correctamente.")
        else:
            print("[Error] El usuario no tiene prestado ese libro.")

    # --- Búsquedas ---
    def buscar_libro_por_titulo(self, titulo):
        return [libro for libro in self._libros_disponibles.values() if titulo.lower() in libro.titulo.lower()]

    def buscar_libro_por_autor(self, autor):
        return [libro for libro in self._libros_disponibles.values() if autor.lower() in libro.autor.lower()]

    def buscar_libro_por_categoria(self, categoria):
        return [libro for libro in self._libros_disponibles.values() if categoria.lower() in libro.categoria.lower()]

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self._usuarios:
            return self._usuarios[id_usuario].libros_prestados
        print("[Error] Usuario no encontrado.")
        return None