estudiantes = {}

def registro_estudiantes():
    a = False
    while a == False:
        cantidad = int(input("Cuantos estudiantes desea regristrar: "))
        if cantidad > 0:
            a = True
        else:
            print("La cantidad debe de ser mayor a 0")
    for i in range (cantidad):
        carnet = int(input("Ingrese el carnet: "))
        nombre = input("Ingrese el nombre completo: ")
        a = False
        while a == False:
            edad = int(input("Ingrese la edad: "))
            if edad > 0 and edad < 100:
                a = True
            else:
                print("Edad invalida")
        carrera = input("Ingrese la carrera: ")

        estudiantes[carnet] = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera,
            "cursos":{}
        }

        a = False
        while a == False:
            cantidad2 = int(input("Cuantos cursos desea inscribir: "))
            if cantidad2 > 0:
                a = True
            else:
                print("Cantidad invalida")
        for x in range(cantidad2):
            nombre_curso = input("\nIngrese el nombre del curso: ")
            a = False
            while a == False:
                nota_tarea = float(input("Ingrese la nota de tareas de (0 - 100): "))
                if nota_tarea >= 0 and nota_tarea <= 100:
                    a = True
                else:
                    print("Nota invalida")
            a = False
            while a == False:
                nota_parcial = float(input("Ingrese la nota de parcial (0 - 100): "))
                if nota_parcial >= 0 and nota_parcial <= 100:
                    a = True
                else:
                    print("Nota invalida")
            a = False
            while a == False:
                nota_proyecto = float(input("Ingrese la nota del proyecto (0 - 100): "))
                if nota_proyecto >= 0 and nota_proyecto <= 100:
                    a = True
                else:
                    print("Nota invalida")

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
        for i in estudiantes:
            print(f"\nNombre: {estudiantes[i]['nombre']}, Carnet: {estudiantes[i]['carnet']}, Edad: {estudiantes[i]['edad']}, Carrera: {estudiantes[i]['carrera']}")
            print(f"Cursos: ")
            for curso in estudiantes[i]["cursos"]:
                nota_tarea = estudiantes[i]["cursos"][curso]["nota_tarea"]
                nota_parcial = estudiantes[i]["cursos"][curso]["nota_parcial"]
                nota_proyecto = estudiantes[i]["cursos"][curso]["nota_proyecto"]
                promedio = (nota_tarea + nota_parcial + nota_proyecto) / 3
                print(f"-{curso}-")
                print(f"Nota de tarea: {nota_tarea}")
                print(f"Nota de parcial: {nota_parcial}")
                print(f"Nota de proyecto: {nota_proyecto}")
                print(f"Promedio: {promedio}")
    else:
        print("No hay estudiantes registrados")

def busqueda_carnet():
    print("====Buscar estudiante====")
    buscar = int(input("Ingrese el carnet del estudiante: "))
    if buscar in estudiantes:
        print(f"Nombre: {estudiantes[buscar]['nombre']}, Edad: {estudiantes[buscar]['edad']}, Carrera: {estudiantes[buscar]['carrera']}")
        print("Cursos:")
        for curso, notas in estudiantes[buscar]["cursos"].items():
            print(f"\n-{curso}-")
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