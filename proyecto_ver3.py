def padres_primerizos():
    print("\nInformacion para padres primerizos")
    print("1. Tramites del bebe")
    print("2. Vacunas")
    print("3. Cuidados basicos")

    op2 = int(input("Opcion: "))

    if op2 == 1:
        print("\nRegistrar al bebe")
        print("Sacar el CURP")
        print("Tramitar cartilla de vacunacion")

    elif op2 == 2:
        print("\nHepatitis B")
        print("BCG")
        print("Consulte un medico para mas informacion")

    elif op2 == 3:
        print("\nLactancia al bebe cada 2-3 horas al dia")
        print("Cambio de pañal cada 3 horas")
        print("Baño de 2-3 veces a la semana")

    else:
        print("Opcion no valida")


def adolescentes():
    print("\nInformacion para adolescentes")
    print("1. Becas")
    print("2. Ayuda con problemas")
    print("3. Metodos anticonceptivos")

    op2 = int(input("Opcion: "))

    if op2 == 1:
        print("\nBeca Benito Juarez (prepa)")
        print("Beca Rita Cetina (secundaria)")
        print("Beca Jovenes Construyendo el Futuro (18 años o mas)")

    elif op2 == 2:
        print("\nAcude con un psicologo")
        print("Pide ayuda con tus maestros")

    elif op2 == 3:
        print("\nCondones")
        print("Pastillas anticonceptivas")
        print("Parches")
        print("Para mas informacion acude con un doctor")

    else:
        print("Opcion no valida")


def adultos_mayores():
    print("\nAdultos mayores")
    print("1. Programas de apoyo")
    print("2. Salud")
    print("3. Alimentacion y cuidados")

    op2 = int(input("Opcion: "))

    if op2 == 1:
        print("\nBienestar Adultos Mayores de 65")
        print("INAPAM")
        print("Pension Mujeres Bienestar")

    elif op2 == 2:
        print("\nRealizar chequeos si presenta molestias")
        print("Acudir al medico minimo 5 veces al mes")
        print("Evitar exponerse al sol")

    elif op2 == 3:
        print("\nComer muchas frutas y verduras")
        print("Evitar realizar actividades peligrosas")
        print("Evitar realizar movimientos bruscos")

    else:
        print("Opcion no valida")


def menu():
    opcion = 0

    while opcion != 4:
        print("\n=== MENU DE AYUDA PARA TODAS LAS PERSONAS ===")
        print("1. Padres primerizos")
        print("2. Adolescentes")
        print("3. Adultos mayores")
        print("4. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            padres_primerizos()

        elif opcion == 2:
            adolescentes()

        elif opcion == 3:
            adultos_mayores()

        elif opcion == 4:
            print("GRACIAS POR USAR EL PROGRAMA")

        else:
            print("Opcion no valida")


menu()
