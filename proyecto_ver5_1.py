from tkinter import *

def mostrar_info(titulo, texto):
    v3 = Toplevel()
    v3.title(titulo)
    v3.geometry("300x250")

    Label(v3, text=titulo).pack()

    Label(v3, text=texto).pack()

    Button(
        v3,
        text="Cerrar",
        command=lambda:[v3.destroy(), v2.destroy()]
    ).pack()


def padres():
    global v2

    v2 = Toplevel()
    v2.title("Padres")
    v2.geometry("300x250")

    Label(v2, text="Padres primerizos").pack()

    Button(
        v2,
        text="Tramites del bebe",
        command=lambda: mostrar_info(
            "Tramites",
            "Registrar al bebe\nSacar CURP\nCartilla de vacunacion"
        )
    ).pack()

    Button(
        v2,
        text="Vacunas",
        command=lambda: mostrar_info(
            "Vacunas",
            "Hepatitis B\nBCG\nConsultar medico"
        )
    ).pack()

    Button(
        v2,
        text="Cuidados basicos",
        command=lambda: mostrar_info(
            "Cuidados",
            "Lactancia\nCambio de pañal\nBaño"
        )
    ).pack()


def adolescentes():
    global v2

    v2 = Toplevel()
    v2.title("Adolescentes")
    v2.geometry("300x250")

    Label(v2, text="Informacion para adolescentes").pack()

    Button(
        v2,
        text="Becas",
        command=lambda: mostrar_info(
            "Becas",
            "Benito Juarez\nRita Cetina\nJovenes Construyendo el Futuro"
        )
    ).pack()

    Button(
        v2,
        text="Ayuda",
        command=lambda: mostrar_info(
            "Ayuda",
            "Hablar con psicologo\nHablar con maestros"
        )
    ).pack()

    Button(
        v2,
        text="Metodos anticonceptivos",
        command=lambda: mostrar_info(
            "Metodos",
            "Condones\nPastillas\nParches"
        )
    ).pack()


def adultos():
    global v2

    v2 = Toplevel()
    v2.title("Adultos mayores")
    v2.geometry("300x250")

    Label(v2, text="Adultos mayores").pack()

    Button(
        v2,
        text="Programas",
        command=lambda: mostrar_info(
            "Programas",
            "Bienestar\nINAPAM\nPension Mujeres Bienestar"
        )
    ).pack()

    Button(
        v2,
        text="Salud",
        command=lambda: mostrar_info(
            "Salud",
            "Chequeos medicos\nIr al medico\nEvitar mucho sol"
        )
    ).pack()

    Button(
        v2,
        text="Alimentacion",
        command=lambda: mostrar_info(
            "Alimentacion",
            "Frutas y verduras\nCuidado al caminar\nEvitar riesgos"
        )
    ).pack()


ventana = Tk()
ventana.title("Menu")
ventana.geometry("300x250")

Label(ventana, text="Menu ayuda para todas las personas").pack()

Button(ventana, text="Padres primerizos", command=padres).pack()

Button(ventana, text="Adolescentes", command=adolescentes).pack()

Button(ventana, text="Adultos mayores", command=adultos).pack()

Button(ventana, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()
