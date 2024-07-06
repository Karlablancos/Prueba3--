import csv

lista_estudiantes = []

# 1 Procesar lista de estudiantes.
def procesar_lista_estudiante():
    if lista_estudiantes:
        print("\nLista de estudiantes: ")
        for estudiante in lista_estudiantes: 
            print(f"Rut: {estudiante['rut']}")
            print(f"Nombre: {estudiante['Nombre']} {estudiante['apellido']}")
            print(f"Nota1: {estudiante['Nota1']}")
            print(f"Nota2: {estudiante['Nota2']}")
    else:
        print("No hay estudiantes registrados. ")

#2.Registrar estudiante.
            
def registrar_estudiante():
    rut = float(input("Ingrese el rut del estudiante: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    nota1 = float(input("Ingrese la nota 1 del estudiante: "))
    nota2 = float(input("Ingrese la nota 2 del estudiante: "))

    lista_estudiantes.append({
        "rut": rut,
        "nombre": nombre,
        "apellido": apellido,
        "nota1": float(nota1),
        "nota2": float(nota2)
    })
    print(f"Estudiante {nombre} {apellido} registrado con éxito")


#3. Modificar nota.

def modificar_nota():
    rut = float(input("Ingrese el rut del estudiante: "))
    nota1 = float(input("Ingrese la nota 1 que desea modificar: "))
    nota2 = float(input("Ingrese la nota 2 que desea modificar: "))
    nuevanota= float(input("Ingrese la nueva nota: "))


    lista_estudiantes.append({
        "rut": float(rut),
        "nota 1": float(nota1),
        "nota 2": float(nota2),
        "nueva nota": float(nuevanota),
    })
    print(f"La nota del/la estudiante {rut} ha sido modificada con éxito")


#4. Eliminar estudiante.
def eliminar_estudiante():
    rut = float(input("Ingrese el rut del estudiante que desea eliminar: "))
    print(f"¿Está seguro de eliminar al estudiante {rut} del sistema? ")

    lista_estudiantes.append({
        "rut": float(rut),
    })
    print(f"La eliminación del/la estudiante {rut} ha sido registrada con éxito")

#5.Generar promedio de notas.
#pipipipipi

#6. Generar acta de cierre de curso. 

def acta_de_cierre_de_curso_csv():
    with open('Acta_cierre_5B.csv', 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(["Rut", "Nombre", "Apellido", "Nota1", "Nota2", "Promedio", "Estado"])
        for estudiante in lista_estudiantes:
            escritor.writerow([estudiante["rut"], estudiante["Nombre"], estudiante["Apellido"], estudiante["Nota1"], estudiante["Nota2"], estudiante["Promedio"], estudiante["Estado"]])
            print("Estudiantes guardados correctamente en Acta_cierre_5B.csv.")

def leer_estudiantes_csv():
    try:
        with open('Acta_cierre_5B.csv', 'r') as archivo_csv:
            lector = csv.reader(archivo_csv)
            next(lector)
            for fila in lector:
                rut, nombre, apellido, nota1, nota2, promedio, estado = fila
                lista_estudiantes.append({
                    "Rut": float(rut),
                    "Nombre": nombre,
                    "Apellido": apellido,
                    "Nota1": float(nota1),
                    "Nota2": float(nota2),
                    "Promedio": float(promedio),
                    "Estado": (estado)
                })
        print("Estudiantes leídos desde Acta_cierre_5B.csv.")
    except ValueError:
        print("El archivo Acta_cierre_5B.csv no existe, vuelva a intentarlo")

#7. Salir del programa. 

while True:
    print("\nMenú Principal: ")
    print("1. Procesar lista de estudiantes.")
    print("2. Registrar estudiante.")
    print("3. Modificar nota.")
    print("4. Eliminar estudiante.")
    print("5. Generar promedio de notas.")
    print("6. Generar acta de cierre de curso.")
    print("7. Salir.")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        procesar_lista_estudiante()
    elif opcion == '2':
        registrar_estudiante()
    elif opcion == '3':
        modificar_nota()
    elif opcion == '4':
        eliminar_estudiante()
    elif opcion == '6':
        acta_de_cierre_de_curso_csv()
    elif opcion == '7':
        print("¡Hasta Luego!")
        break
    else:
        print("Opción inválida.")

