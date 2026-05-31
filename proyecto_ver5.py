from tkinter import *

def abrir_menu_padres():
    ventana_padres = Toplevel(ventana)
    ventana_padres.title("Menu Padres Primerizos")
    ventana_padres.geometry("400x300")
    
    Label(ventana_padres, text="OPCIONES PARA PADRES").pack(pady=10)
    
    Label(ventana_padres, text="- Registrar al bebe").pack(pady=5)
    Label(ventana_padres, text="- Sacar CURP").pack(pady=5)
    Label(ventana_padres, text="- Cartilla de vacunacion").pack(pady=5)
    Label(ventana_padres, text="- Vacunas Hepatitis B y BCG").pack(pady=5)
    
    Button(ventana_padres, text="Cerrar", command=ventana_padres.destroy).pack(pady=20)

def abrir_menu_adolescentes():
    ventana_ados = Toplevel(ventana)
    ventana_ados.title("Menu Adolescentes")
    ventana_ados.geometry("400x300")
    
    Label(ventana_ados, text="OPCIONES PARA ADOLESCENTES").pack(pady=10)
    
    Label(ventana_ados, text="- Beca Benito Juarez").pack(pady=5)
    Label(ventana_ados, text="- Beca Rita Cetina").pack(pady=5)
    Label(ventana_ados, text="- Acudir con un psicologo").pack(pady=5)
    Label(ventana_ados, text="- Condones y otros metodos anticonceptivos").pack(pady=5)
    
    Button(ventana_ados, text="Cerrar", command=ventana_ados.destroy).pack(pady=20)

def abrir_menu_adultos():
    ventana_adultos = Toplevel(ventana)
    ventana_adultos.title("Menu Adultos Mayores")
    ventana_adultos.geometry("400x300")
    
    Label(ventana_adultos, text="OPCIONES PARA ADULTOS MAYORES").pack(pady=10)
    
    Label(ventana_adultos, text="- INAPAM").pack(pady=5)
    Label(ventana_adultos, text="- Pension Bienestar").pack(pady=5)
    Label(ventana_adultos, text="- Alimentacion saludable").pack(pady=5)
    Label(ventana_adultos, text="- Chequeos medicos frecuentes").pack(pady=5)
    
    Button(ventana_adultos, text="Cerrar", command=ventana_adultos.destroy).pack(pady=20)


ventana = Tk()
ventana.title("Menu de Ayuda")
ventana.geometry("400x350")

Label(ventana, text="MENU DE AYUDA").pack(pady=15)

Button(ventana, text="1. Padres primerizos", width=25, command=abrir_menu_padres).pack(pady=5)
Button(ventana, text="2. Adolescentes", width=25, command=abrir_menu_adolescentes).pack(pady=5)
Button(ventana, text="3. Adultos mayores", width=25, command=abrir_menu_adultos).pack(pady=5)

Button(ventana, text="4. Salir", width=25, command=ventana.quit).pack(pady=20)

ventana.mainloop()
        
