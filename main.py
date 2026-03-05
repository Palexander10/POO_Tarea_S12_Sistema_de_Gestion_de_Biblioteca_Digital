from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio

def mostrar_menu():
    print("\n--- SISTEMA DE BIBLIOTECA DIGITAL ---")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados de un usuario")
    print("9. Salir")
    print("-------------------------------------")

def main():
    # Inicialización del servicio
    biblioteca = BibliotecaServicio()

    # Algunos datos de prueba para que puedas evaluar el sistema rápidamente
    biblioteca.anadir_libro(Libro("Fundamentos de Programación", "Luis Joyanes", "Tecnología", "ISBN-101"))
    biblioteca.anadir_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "ISBN-102"))
    biblioteca.registrar_usuario(Usuario("Pablo Alexander", "U001"))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.anadir_libro(Libro(titulo, autor, categoria, isbn))

        elif opcion == '2':
            isbn = input("ISBN del libro a retirar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID único (ej. U002): ")
            biblioteca.registrar_usuario(Usuario(nombre, id_usuario))

        elif opcion == '4':
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '5':
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '6':
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '7':
            print("Buscar por: [a] Título  [b] Autor  [c] Categoría")
            sub = input("Opción: ").lower()
            termino = input("Término a buscar: ")
            
            resultados = []
            if sub == 'a': resultados = biblioteca.buscar_libro_por_titulo(termino)
            elif sub == 'b': resultados = biblioteca.buscar_libro_por_autor(termino)
            elif sub == 'c': resultados = biblioteca.buscar_libro_por_categoria(termino)
            
            if resultados:
                print("\n--- Resultados ---")
                for r in resultados: print(r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == '8':
            id_usuario = input("ID del usuario: ")
            libros = biblioteca.listar_libros_prestados(id_usuario)
            if libros:
                print(f"\n--- Libros prestados ---")
                for lib in libros: print(lib)
            elif libros is not None and len(libros) == 0:
                print("El usuario no tiene libros prestados actualmente.")

        elif opcion == '9':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()