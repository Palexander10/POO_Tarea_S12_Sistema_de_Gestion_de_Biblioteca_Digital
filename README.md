# Sistema de Gestión de Biblioteca Digital 📚

Estudiante:Pablo Alexander Ramón Mosquera

Este proyecto es un sistema de gestión de biblioteca digital desarrollado en Python, aplicando los principios de la **Programación Orientada a Objetos (POO)** y una **arquitectura estructurada por capas**. 

Esta tarea demuestra la separación de responsabilidades entre los datos, la lógica de negocio y la interfaz de usuario.

## 🏗️ Arquitectura del Proyecto

El sistema respeta una estructura de carpetas modular:

* **`modelos/`**: Contiene las clases que representan las entidades del sistema (`Libro` y `Usuario`). Aquí se define la estructura de los datos, aplicando encapsulamiento (getters) y utilizando estructuras inmutables (tuplas) donde es requerido.
* **`servicios/`**: Contiene la clase `BibliotecaServicio`. Es el corazón del sistema, donde reside toda la lógica de negocio, validaciones y administración de colecciones mediante diccionarios y conjuntos (sets).
* **`main.py`**: Es el punto de arranque del programa. Implementa un menú interactivo en consola para probar el sistema y delega las operaciones a la capa de servicios. No contiene lógica de negocio.

## ✨ Funcionalidades Principales

* **Gestión del Catálogo**: Añadir y retirar libros del sistema.
* **Gestión de Usuarios**: Registrar nuevos usuarios y darlos de baja (con validación de devoluciones pendientes).
* **Préstamos y Devoluciones**: Prestar libros disponibles a usuarios registrados y gestionar su retorno al catálogo.
* **Búsquedas**: Encontrar libros rápidamente por título, autor o categoría.
* **Auditoría**: Listar los libros que un usuario específico tiene prestados actualmente.

## 🛠️ Tecnologías y Estructuras de Datos

* **Lenguaje**: Python 3.x
* **Estructuras utilizadas**:
  * `Tuplas`: Para almacenar datos inmutables como el título y autor del libro.
  * `Listas`: Para el registro de libros prestados a cada usuario.
  * `Diccionarios`: Para almacenar los libros disponibles en la biblioteca (Clave: ISBN).
  * `Sets (Conjuntos)`: Para gestionar y validar los IDs únicos de los usuarios.

