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
    