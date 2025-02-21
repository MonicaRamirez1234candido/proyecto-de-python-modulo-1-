#diccionario de almacenaje de libros 
libros = {}

#función que agrega libros 
def agregar_libro ():
    print("Agregar nuevo libro")
    
    # Diccionario para almacenar libros (con tupla como clave)
libros = {}

# Función para agregar un libro
def agregar_libro():
    print("\n Agregar libro\n")
    
    # Inputs para la interacción del usuario 
    titulo = input("Escribe el título del libro: ")
    autor = input("Agrega el nombre del autor del libro: ")
    disponibilidad = input("¿Está disponible? (sí/no): ").lower() == "sí"
    
    # Crear clave como tupla (título, autor) y asignar disponibilidad
    libros[(titulo, autor)] = disponibilidad
    print(f"Libro '{titulo}' de {autor} agregado correctamente.")

# Función para buscar libros
def buscar_libro():
    clave = input("¿Quieres buscar por título o autor? (título/autor): ").lower()
    
    if clave == 'título':
        titulo = input("Introduce el título del libro: ")
        encontrado = False
        for (t, a), disponible in libros.items():
            if t.lower() == titulo.lower():
                print(f"Título: {t}, Autor: {a}, Disponible: {disponible}")
                encontrado = True
        if not encontrado:
            print("No se ha encontrado el libro.")
    elif clave == 'autor':
        autor = input("Introduce el nombre del autor: ")
        encontrados = False
        for (t, a), disponible in libros.items():
            if a.lower() == autor.lower():
                print(f"Título: {t}, Autor: {a}, Disponible: {disponible}")
                encontrados = True
        if not encontrados:
            print("No se han encontrado libros de este autor.")
    else:
        print("Opción no válida.")

# Función para ver todos los libros registrados
def ver_todos_libros():
    if libros:
        print("Lista de libros registrados:")
        for (titulo, autor), disponibilidad in libros.items():
            print(f"Título: {titulo}, Autor: {autor}, Disponible: {disponibilidad}")
    else:
        print("No hay libros registrados.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Ver todos los libros")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            ver_todos_libros()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()