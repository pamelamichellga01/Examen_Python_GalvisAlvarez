from interfaz import menu_1_simulador_propina,menu_2_calculo_propina, menu_3_total_pagar_dividido,menu_4
def main():
    while True:
        menu_1_simulador_propina()
        opcion = int(input("Por favor, elige una opción (1-3):"))

        if opcion == 1:
            menu_2_calculo_propina()
        elif opcion == 2:
            menu_3_total_pagar_dividido()
        elif opcion == 3:
            menu_4()
            break
        else:
            print('Opcion no valida.')


main()