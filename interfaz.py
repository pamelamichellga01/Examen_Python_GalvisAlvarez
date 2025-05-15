from calculos import calcular_propina, calcular_total_con_propina, dividir_total, mostrar_resultados

def menu_1_simulador_propina():
    print("=============================================")
    print("SIMULADOR DE PROPINA")
    print("=============================================")
    print("1. Calcular propina y total a pagar")
    print("2. Calcular total a pagar divido entre varias personas")
    print("3. Salir")
    print("=============================================")

def datos_calculo_propina():
    print("=============================================")
    print("Cálculo de Propina")
    print("=============================================")

    total=float(input("Ingrese el monto total de la cuenta: $"))
    porcentaje=(float(input("Ingrese el porcentaje de propina (por ejemplo: 15):")))
    propina=calcular_propina(total,porcentaje)

    print("=============================================")

    print(f"La propina calculada es: ${propina:.2f} ")
    total_mas_propiena=calcular_total_con_propina(total,propina)
    print(f"El total a pagar es: ${total_mas_propiena:.2f}")

    print("=============================================")


def menu_2_calculo_propina():
    
    while True:

        datos_calculo_propina()

        repetir_calculo=input("¿Deseas calcular nuevamente? (S/N)").lower()

        if repetir_calculo == "s":
            print("¡POR SU PUESTO!")

        elif repetir_calculo=="n":
            print(f'Gracias por visitar')
            break
        else:
            print('Opcion no valida.')

def datos_dividir_personas():
    print("============================================")
    print(" Dividir Cuenta entre Varias Personas")
    print("============================================")
    
    while True:
        total=float(input("Ingrese el monto total de la cuenta: $"))

        if total > 0:
            break
        elif total == 0:
            print("La cuenta no puede ser 0. Intentalo neuvamente.")
        else:
            print("El total no puede ser negativo (-)")


    porcentaje=(float(input("Ingrese el porcentaje de propina (por ejemplo: 15):"))) 
    personas=int(input("Ingrese el número de personas:"))

    print("============================================")

    propina=calcular_propina(total,porcentaje)
    print(f"La propina calculada es: ${propina}")

    total_mas_propiena=calcular_total_con_propina(total,propina)
    print(f"El total a pagar es: ${total_mas_propiena:.2f}")

    dividido=dividir_total(total_mas_propiena,personas)
    print(f"Monto por persona: ${dividido:.2f}")

    print("=============================================")
    
def menu_3_total_pagar_dividido():
    while True:

        datos_dividir_personas()

        repetir_calculo=input("¿Deseas calcular nuevamente? (S/N)").lower()

        if repetir_calculo == "s":
            print("¡POR SU PUESTO!")

        elif repetir_calculo=="n":
            print(f'Gracias por visitar')
            break
        else:
            print('Opcion no valida.')

    return

def menu_4():
    print("=============================================")
    print("¡Gracias por usar el Simulador de Propina!")
    print("=============================================")

