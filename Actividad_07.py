estudiantes = {}

def registro_estudiantes():
    cantidad = int(input("Cuantos estudiantes desea regristrar: "))
    for i in range (cantidad):
        carnet = int(input("Ingrese el carnet: "))
        nombre = input("Ingrese el nombre completo: ")
        edad = int(input("Ingrese la edad: "))
        carrera = input("Ingrese la carrera: ")

        estudiantes[carnet] = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera,
            "cursos":{}
        }

        cantidad2 = int(input("Cuantos cursos desea inscribir: "))
        for x in range(cantidad2):
            nombre_curso = input("\nIngrese el nombre del curso: ")
            nota_tarea = float(input("Ingrese la nota de tareas de (0 - 100): "))
            nota_parcial = float(input("Ingrese la nota de parcial (0 - 100): "))
            nota_proyecto = float(input("Ingrese la nota del proyecto (0 - 100): "))

            estudiantes[carnet]["cursos"][nombre_curso] = {
                "nota_tarea": nota_tarea,
                "nota_parcial": nota_parcial,
                "nota_proyecto": nota_proyecto
            }
            print("\nSe ha registrado el curso")
        print("\nSe ha registrado el estudiante")

def mostrar_estudiantes_cursos():
    print("====Estudiantes inscritos===")
    if len(estudiantes) > 0:
        for i, datos in estudiantes.items():
            print(f"Nombre: {estudiantes[i]['nombre']}, Edad: {estudiantes[i]['edad']}, Carrera: {estudiantes[i]['carrera']}")
    else:
        print("No hay estudiantes registrados")

def busqueda_carnet():
    print("====Buscar estudiante====")
    buscar = int(input("Ingrese el carnet del estudiante: "))
    if buscar in estudiantes:
        print(f"Nombre: {estudiantes[buscar]['nombre']}, Edad: {estudiantes[buscar]['edad']}, Carrera: {estudiantes[buscar]['carrera']}")
        print("Cursos:")
        for curso, notas in estudiantes[buscar]["cursos"].items():
            print(f"{curso}")
            print(f"Nota de tarea: {notas['nota_tarea']}")
            print(f"Nota de parcial: {notas['nota_parcial']}")
            print(f"Nota de proyecto: {notas['nota_proyecto']}")
    else:
        print("Estudiante no encontrado")

opciones = 0
e = False
while e == False:
    print("====Menu====")
    print("1. Registrar estudiantes")
    print("2. Mostrar todos los estudiantes y sus cursos")
    print("3. Buscar estudiante por carnet")
    print("4. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            registro_estudiantes()
        case 2:
            mostrar_estudiantes_cursos()
        case 3:
            busqueda_carnet()
        case 4:
            print("Gracias por usar el sistema")
            e = True
        case _:
            print("Opcion invalida")