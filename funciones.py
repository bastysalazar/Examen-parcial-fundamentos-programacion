#Evaluacion final transversal
#funciones sistema FitPass
#Funcion del menu
def mostrar_menu():
    print("\n------- MENÚ PRINCIPAL --------")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("---------------------------------")

#leer opcion del Menu
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
            else:
                return opcion
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

#Buscar codigo
def buscar_codigo(planes, codigo):
    codigo = codigo.upper()
    for cod in planes:
        if cod.upper() == codigo:
            return True
    return False

#Validaciones
def validar_codigo(planes, codigo):
    if codigo.strip() == "":
        return False
    if buscar_codigo(planes, codigo):
        return False
    return True

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True

def validar_tipo(tipo):
    tipo = tipo.strip().lower()
    if tipo == "mensual":
        return True
    if tipo == "trimestral":
        return True
    if tipo == "anual":
        return True
    return False

def validar_duracion(duracion_meses):
        if duracion_meses > 0:
            return True
        return False

def validar_acceso_piscina(acceso_piscina):
    acceso_piscina = acceso_piscina.lower()
    if acceso_piscina == "s" or acceso_piscina == "n":
        return True
    return False

def validar_incluye_clases(incluye_clases):
    incluye_clases = incluye_clases.lower()
    if incluye_clases == "s" or incluye_clases == "n":
        return True
    return False

def validar_horario(horario):
    if horario.strip() == "":
        return False
    return True

def validar_precio(precio):
        if precio > 0:
            return True
        return False

def validar_cupos(cupos):
        if cupos >= 0:
            return True
        return False

#Cupos por tipo de plan
def cupos_tipo(tipo, planes, inscripciones):
    tipo = tipo.lower()
    total = 0
    for codigo in planes:
        if planes [codigo][1].lower() == tipo:
            total += inscripciones[codigo][1]
    print(f"El total de cupos disponibles es: {total}")

#Busqueda por rango de precio
def busqueda_precio(precio_minimo, precio_maximo, planes, inscripciones):
    encontrados = []
    for codigo in inscripciones:
        precio = inscripciones[codigo][0]
        cupos = inscripciones[codigo][1]
        if precio_minimo <= precio <= precio_maximo and cupos > 0:
            nombre =  planes[codigo][0]
            encontrados.append(nombre + "--" + codigo)
    encontrados.sort()
    if len(encontrados) == 0:
        print("No hay planes en ese rango de precios.")
    else:
        print ("Los planes encontrados son:")
        print (encontrados)

#Actualizar precio
def actualizar_precio(planes, inscripciones, codigo, nuevo_precio):
    codigo = codigo.upper()
    if not buscar_codigo(planes, codigo):
        return False
    inscripciones[codigo][0] = nuevo_precio
    return True

#Agregar plan
def agregar_plan(planes,
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
    codigo = codigo.upper()
    if buscar_codigo(planes, codigo):
        return False
#Convirtiendo s/n a booleandos
    if acceso_piscina.lower() == "s":
        acceso_piscina = True
    else:
        acceso_piscina = False

    if incluye_clases.lower() == "s":
        incluye_clases = True
    else:
        incluye_clases = False

    planes[codigo] =[
        nombre_plan,
        tipo.lower(),
        duracion_meses,
        acceso_piscina,
        incluye_clases,
        horario
    ]
    inscripciones[codigo] = [
        precio,
        cupos
    ]
    return True

#Eliminar plan
def eliminar_plan(planes, inscripciones, codigo):
    codigo = codigo.upper()
    if not buscar_codigo(planes, codigo):
        return False
    del planes[codigo]
    del inscripciones[codigo]
    return True