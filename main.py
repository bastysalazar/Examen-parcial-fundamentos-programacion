from funciones import *

#Diccionarios
planes = {"F001": ["Plan Básico", "mensual", 1, False, False, "libre"],
    "F002": ["Plan Full", "mensual", 1, True, True, "libre"],
    "F003": ["Plan Estudiante", "trimestral", 3, False, True, "tarde"],
    "F004": ["Plan Senior", "trimestral", 3, True, False, "mañana"],
    "F005": ["Plan Anual Pro", "anual", 12, True, True, "libre"],
    "F006": ["Plan Nocturno", "mensual", 1, False, True, "noche"]
    }

inscripciones = {
    "F001": [14990, 30],
    "F002": [22990, 10],
    "F003": [39990, 0],
    "F004": [35990, 6],
    "F005": [159990, 2],
    "F006": [18990, 15]
}

#Programa main
while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        tipo = input("Ingrese el tipo de plan a consultar: ")
        cupos_tipo(tipo, planes, inscripciones)

    elif opcion == 2:
        while True:
            try:
                precio_minimo = int(input("Ingrese el precio minimo: "))
                precio_maximo = int(input("Ingrese el precio maximo: "))
                if precio_minimo >= 0 and precio_maximo >= 0 and precio_minimo <= precio_maximo:
                    break
                print ("Los valores ingresados no son validos")
            except ValueError:
                print("Debe ingresar un numero entero positivo")
        busqueda_precio(precio_minimo, precio_maximo, planes, inscripciones)

    elif opcion == 3:
        while True:
            codigo = input("Ingrese el codigo del plan: ")
            while True:
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    if nuevo_precio > 0:
                        break
                    print ("¡El precio debe ser mayor que 0!")
                except ValueError:
                    print ("¡Debe ingresar un numero entero positivo!")
            if actualizar_precio(planes, inscripciones, codigo, nuevo_precio):
                print ("¡Precio actualizado correctamente!")
            else:
                print ("El codigo no existe")
            respuesta = input("¿Desea actualizar otro precio (s/n)? ").lower()
            if respuesta == "n":
                break
    
    elif opcion == 4:
        codigo = input("Ingrese el codigo del plan: ")
        nombre_plan = input("Ingrese el nombre del plan: ")
        tipo = input("Ingrese el tipo (mensual/trimestral/anual): ").lower()
        try:
            duracion_meses = int(input("Ingrese duracion (meses): "))
        except ValueError:
            duracion_meses = 0
        acceso_piscina = input("¿Incluye acceso a la picina? (s/n): ").lower()
        incluye_clases = input("¿Incluye clases grupales? (s/n): ").lower()
        horario = input("Ingrese horario: ")
        try:
            precio = int(input("Ingrese precio: "))
        except ValueError:
            precio = 0
        try:
            cupos = int(input("Ingrese cupos: "))
        except ValueError:
            cupos = -1
        if not validar_codigo(planes, codigo):
            print ("Codigo invalido o ya existente")
        elif not validar_nombre(nombre_plan):
            print("Nombre invalido")
        elif not validar_tipo(tipo):
            print ("Tipo invalido")
        elif not validar_duracion(duracion_meses):
            print ("Duracion Invalida")
        elif not validar_acceso_piscina(acceso_piscina):
            print("Debe ingresar s/n para acceso a picina")
        elif not validar_incluye_clases(incluye_clases):
            print("Debe ingresar s/n para incluye clases")
        elif not validar_horario(horario):
            print("Horario invalido")
        elif not validar_precio(precio):
            print("Precio invalido")
        elif not validar_cupos(cupos):
            print("Cantidad de cupos invalida")
        else:
            if agregar_plan(planes,
                            inscripciones,
                            codigo,
                            nombre_plan,
                            tipo,
                            duracion_meses,
                            acceso_piscina,
                            incluye_clases,
                            horario,
                            precio,
                            cupos):
                print ("Plan agregado con exito")
            else:
                print("El codigo ya existe")

    elif opcion == 5:
        codigo = input("Ingrese el codigo del plan: ")
        if eliminar_plan(planes, inscripciones, codigo):
            print("Plan eliminado")
        else:
            print("El codigo no existe")

    else:
        print("Programa finalizado")
        break