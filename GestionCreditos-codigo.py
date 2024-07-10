import random
import csv

alumnos = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
    "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
    ]

creditos_alumnos = {}


def asignacion_creditos(alumnos):
    for alumno in alumnos:
        credito = random.randint(50,200)
        creditos_alumnos[alumno] = credito

    print("Creditos asignados correctamente")
    print(creditos_alumnos)

    return creditos_alumnos

def clasificacion_creditos(creditos_alumnos):
    menor = {} #menor a 100
    mid = {} #entre 100 y 150
    mayor = {} #mayor a 150

    for alumno,credito in creditos_alumnos.items():
        if credito < 100:
            menor[alumno] = credito
        elif credito <= 150:
            mid[alumno] = credito
        else:
            mayor[alumno] = credito

    print("- Creditos inferiores a 100: ",len(menor))
    for alumno, credito in menor.items():
        print(alumno, ": $", credito)
    print("- Creditos entre 100 y 150: ",len(mid))
    for alumno, credito in mid.items():
        print(alumno, ": $", credito)
    print(" Creditos superiores a 150: ",len(mayor))
    for alumno, credito in mayor.items():
        print(alumno, ": $", credito)


def calculo_estadisticas(creditos_alumnos):
    creditos = list(creditos_alumnos.values())
    if not creditos:
        print("No se han encontrado creditos asignados. Debe asignar primero.")
        return None, None, None
    
    credito_minimo = min(creditos)
    credito_maximo = max(creditos)
    credito_promedio = sum(creditos) / len(creditos)

    return credito_minimo, credito_maximo, credito_promedio

def generar_reporte(creditos_alumnos):
    with open('reportes_creditos.csv','w', newline='') as archivo:
        escritor = csv.writer(archivo, delimiter=',')
        escritor.writerow(['Nombre alumno:','Credito:'])

        for alumno, credito in creditos_alumnos.items():
            escritor.writerow([alumno, credito])
            print("Reporte creado correctamente en reportes_creditos.csv")
            return
    

while True:
    print("---MENU---")
    print("1. Iniciar creditos")
    print("2. Asignacion de creditos")
    print("3. Clasificar creditos")
    print("4. Calcular estadisticas de los creditos")
    print("5. Generar reporte de los creditos en CSV")
    print("6. Salir del programa")
    try:
        opcion = int(input("Ir a: "))
        if opcion == 1:
            creditos_alumnos = {alumno : 0 for alumno in alumnos}
            print("Creditos inicializados correctamente")
        elif opcion == 2:
            if not creditos_alumnos:
                print("Debe inicializar los creditos primero.")
            else:
                creditos_alumnos = asignacion_creditos(alumnos)
        elif opcion == 3:
            if creditos_alumnos:
                clasificacion_creditos(creditos_alumnos)
            else:
                print("Debe asignar creditos primero.")
        elif opcion == 4:
            if creditos_alumnos:
                credito_minimo, credito_maximo, credito_promedio = calculo_estadisticas(creditos_alumnos)
                if credito_maximo is not None:
                    print("Credito minimo: $",credito_minimo)
                    print("Credito maximo: $",credito_maximo)
                    print("Promedio de creditos: $",credito_promedio)
                else:
                    print("Debe asignar creditos primero")
        elif opcion == 5:
            if creditos_alumnos:
                generar_reporte(creditos_alumnos)
            else:
                print("Debe asignar creditos primero")
        elif opcion == 6:
            print("Saliendo.")
            break
        else:
            print("Debe seleccionar una opcion valida (1-6)")
    except ValueError:
        print("Debe seleccionar una opcion valida (1-6)")
