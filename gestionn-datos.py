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