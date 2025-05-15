def calcular_propina(total, porcentaje):
    return (total*porcentaje)/100

def calcular_total_con_propina(total, propina):
    return total+propina

def dividir_total(total, personas):
    if personas >0:
        return total/personas
    else:
        return total

def mostrar_resultados(propina, total, total_persona):
    return