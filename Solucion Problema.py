# Problema 5 - Horas trabajadas

UMBRAL_HORAS = 40

def calcular_jornada(horas):
    total = sum(horas)

    if total > UMBRAL_HORAS:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


def mostrar_informe(recursos):
    print("INFORME DE HORAS SEMANALES")
    print("-" * 40)

    for recurso in recursos:
        nombre = recurso[0]
        horas = recurso[1:]

        total, clasificacion = calcular_jornada(horas)

        print(f"Recurso: {nombre}")
        print(f"Total de horas: {total}")
        print(f"Clasificación: {clasificacion}")
        print("-" * 40)


recursos = [
    ["Ana", 8, 8, 8, 8, 8],
    ["Carlos", 9, 8, 9, 8, 9],
    ["María", 7, 8, 7, 8, 7],
    ["Pedro", 10, 8, 8, 9, 8]
]

mostrar_informe(recursos)

input("Presiona Enter para cerrar...")
