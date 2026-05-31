from tkinter import *

def mostrar():

    opcion = entrada.get()

    if opcion == "1":
        texto.insert(END, "PADRES PRIMERIZOS\n\n")
        texto.insert(END, "- Registrar al bebe\n")
        texto.insert(END, "- Sacar CURP\n")
        texto.insert(END, "- Cartilla de vacunacion\n")
        texto.insert(END, "- Vacunas Hepatitis B y BCG\n")

    elif opcion == "2":
        texto.insert(END, "ADOLESCENTES\n\n")
        texto.insert(END, "- Beca Benito Juarez\n")
        texto.insert(END, "- Beca Rita Cetina\n")
        texto.insert(END, "- Acudir con un psicologo\n")
        texto.insert(END, "- Condones y otros metodos anticonceptivos\n")

    elif opcion == "3":
        texto.insert(END, "ADULTOS MAYORES\n\n")
        texto.insert(END, "- INAPAM\n")
        texto.insert(END, "- Pension Bienestar\n")
        texto.insert(END, "- Alimentacion saludable\n")
        texto.insert(END, "- Chequeos medicos frecuentes\n")

    elif opcion == "4":
        texto.insert(END, "GRACIAS POR USAR EL PROGRAMA")

    else:
        texto.insert(END, "Opcion no valida")


ventana = Tk()
ventana.title("Menu de Ayuda")
ventana.geometry("450x350")

Label(ventana, text="MENU DE AYUDA").pack()

Label(ventana, text="1. Padres primerizos").pack()
Label(ventana, text="2. Adolescentes").pack()
Label(ventana, text="3. Adultos mayores").pack()
Label(ventana, text="4. Salir").pack()

entrada = Entry(ventana)
entrada.pack()

Button(ventana, text="Mostrar informacion", command=mostrar).pack()

texto = Text(ventana, width=50, height=12)
texto.pack()

ventana.mainloop()
