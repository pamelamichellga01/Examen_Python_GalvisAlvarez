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

    
    while True:
        total=float(input("Ingrese el monto total de la cuenta: $"))

        if total > 0:
            break
        elif total == 0:
            print("La cuenta no puede ser cero (0). Intentalo neuvamente.")
        else:
            print("El total no puede ser negativo (-)")

    while True:        
        porcentaje=(float(input("Ingrese el porcentaje de propina (por ejemplo: 15):")))
        if porcentaje>0 and porcentaje<=100:
            break
        elif porcentaje == 0:
            print("El porcentaje no puede ser cero (0).")
        elif porcentaje <0:
            print("El porcentje no puede tomar valores negativos (-).")
        else:
            print("Valor incorrecto")

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


    while True:        
        porcentaje=(float(input("Ingrese el porcentaje de propina (por ejemplo: 15):")))
        if porcentaje>0 and porcentaje<=100:
            break
        elif porcentaje == 0:
            print("El porcentaje no puede ser cero (0).")
        elif porcentaje <0:
            print("El porcentje no puede tomar valores negativos (-).")
        else:
            print("Valor incorrecto")

    while True:
        personas=int(input("Ingrese el número de personas:"))
        if personas > 0:
            break
        elif personas == 0:
            print("El nuemro de personas no puede ser cero (0).")
        elif personas <0:
            print("El numero de personas no puede tomar valores negativos (-).")
        else:
            print("Valor incorrecto")


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

