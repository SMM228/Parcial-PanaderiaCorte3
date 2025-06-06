import random
import math
PRODUCT_CATALOG = {
    "crescent": "Media Luna",
    "french_loaf": "Baguette",
    "cheese_bread": "Queso Roll"
}


registro_fabricacion = []

def eficiencia_promedio_equipo():
    """
    Calcula el rendimiento promedio del grupo.
    """
    if not registro_fabricacion:
        return 0
    suma = sum(j["rendimiento"] for j in registro_fabricacion)
    return round(suma / len(registro_fabricacion))

def resumen_objetivos():
    """
    Suma los estados de cumplimiento del objetivo de cada jornada.
    """
    logrados = sum(1 for j in registro_fabricacion if j["estado"] == "Logrado")
    no_logrados = len(registro_fabricacion) - logrados
    return {"Logrado": logrados, "No logrado": no_logrados}

def agregar_jornada(laborista, items_hechos):
    """
    Registra una nueva jornada de fabricación de un empleado.

    Argumentos:
        laborista (str): Nombre del empleado.
        items_hechos (dict): Cantidad de cada producto realizado. Ej:
                             {"french_loaf": 80, "cheese_bread": 120, "crescent": 60}
    Retorna:
        dict: Registro completo de la jornada, con indicadores calculados.
        None: Si alguna cantidad fuera de rango.
    """
    detalle_jornada = {}
    denominador_efic = 0
    numerador_efic = 0

    for prod_id, valor in items_hechos.items():
        factor = round(random.uniform(1.0, 1.5), 2)
        if valor < 0 or valor > 500:
            print(f"Cantidad inválida para {PRODUCT_CATALOG.get(prod_id, prod_id)}. Debe estar entre 0 y 500.")
            return None
        detalle_jornada[prod_id] = {
            "factor": factor,
            "unidades": valor
        }
        denominador_efic += factor
        numerador_efic += valor * factor

    
    if denominador_efic == 0:
        indice_efic = 0
    else:
        indice_efic = numerador_efic / denominador_efic
    rendimiento = round(indice_efic)

    estado_objetivo = "Logrado" if rendimiento >= 300 else "No logrado"

    jornada = {
        "detalle": detalle_jornada,
        "trabajador": laborista,
        "rendimiento": rendimiento,
        "estado": estado_objetivo
    }
    registro_fabricacion.append(jornada)
    return jornada

    

def resumen_general():
    """
    Genera un panorama general de jornadas registradas.
    """
    
    return [
        {
            "rendimiento": j["rendimiento"],
            "trabajador": j["trabajador"],
            "estado": j["estado"]
        }
        for j in registro_fabricacion
    ]
