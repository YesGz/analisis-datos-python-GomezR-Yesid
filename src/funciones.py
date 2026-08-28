def convertir_a_float(valor):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return None

def calcular_potencia(voltaje, corriente):
    if voltaje is None or corriente is None:
        return None
    if voltaje < 0 or corriente < 0:
        return None
    return voltaje * corriente

def clasificar_temperatura(temp):
    if temp is None:
        return "Dato inválido"
    elif temp < 40:
        return "Normal"
    elif temp < 50:
        return "Precaución"
    else:
        return "Alerta"