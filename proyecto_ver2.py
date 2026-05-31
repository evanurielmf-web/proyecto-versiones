opcion = 0

while opcion != 4:
    print("Menu ayuda para todas las personas")
    print("Seleccione una opcion:")
    print("1. Padres primerizos")
    print("2. Adolescentes informacion")
    print("3. Adultos mayores")
    print("4. Salir")

    opcion = int(input("Opcion: "))

    if opcion == 1:
        print("Informacion para padres primerizos")
        print("1. Tramites del bebe")
        print("2. Vacunas")
        print("3. Cuidados basicos")

        op2 = int(input("Opcion: "))

        if op2 == 1:
            print("Registrar al bebe")
            print("Sacar el CURP")
            print("Tramitar cartilla de vacunacion")
            print(".......")

        elif op2 == 2:
            print("Hepatitis B")
            print("BCG")
            print("Consulte un medico para mas informacion")
            print(".......")

        elif op2 == 3:
            print("Lactancia al bebe cada 2-3 horas al dia")
            print("Cambio de pañal cada 3 horas")
            print("Baño de 2-3 veces a la semana")
            print(".......")

        else:
            print("Opcion no valida")

    elif opcion == 2:
        print("Informacion para adolescentes")
        print("1. Becas")
        print("2. Ayuda con problemas")
        print("3. Metodos anticonceptivos")

        op2 = int(input("Opcion: "))

        if op2 == 1:
            print("Beca Benito Juarez (prepa)")
            print("Beca Rita Cetina (secundaria)")
            print("Beca Jovenes Construyendo el Futuro (18 años o mas)")
            print(".......")

        elif op2 == 2:
            print("Acude con un psicologo")
            print("Pide ayuda con tus maestros")
            print(".......")

        elif op2 == 3:
            print("Condones")
            print("Pastillas anticonceptivas")
            print("Parches")
            print("Para mas informacion acude con un doctor")
            print(".......")

        else:
            print("Opcion no valida")

    elif opcion == 3:
        print("Adultos mayores")
        print("1. Programas de apoyo")
        print("2. Salud")
        print("3. Alimentacion y cuidados")

        op2 = int(input("Opcion: "))

        if op2 == 1:
            print("Bienestar Adultos Mayores de 65")
            print("INAPAM")
            print("Pension Mujeres Bienestar")
            print(".......")

        elif op2 == 2:
            print("Realizar chequeos si presenta molestias")
            print("Acudir al medico minimo 5 veces al mes")
            print("Evitar exponerse al sol")
            print(".......")

        elif op2 == 3:
            print("Comer muchas frutas y verduras")
            print("Evitar realizar actividades peligrosas")
            print("Evitar realizar movimientos bruscos")
            print(".......")

        else:
            print("Opcion no valida")

    elif opcion == 4:
        print("GRACIAS POR USAR EL PROGRAMA")

    else:
        print("Opcion no valida")
