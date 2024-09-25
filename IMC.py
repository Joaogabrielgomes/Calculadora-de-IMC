from tkinter import *
from tkinter import messagebox

janela = Tk()

def calcular_imc():
    try:
        imc = float(peso.get()) / float(altura.get()) ** 2
        
        if imc < 18.5:
            resultado["text"] = f"O seu IMC é {imc:.2f}, classificado como magreza"
        
        elif 18.51 < imc < 24.9:
            resultado["text"] = f"O seu IMC é {imc:.2f}, classificado como normal"

        else:
            resultado["text"] = f"O seu IMC é {imc:.2f}, classificado como sobrepeso"
            
    
    except ValueError:
        #Label(frame, text="Por favor, insira valores válidos para peso e altura", pady=20).grid(column=1, row=5, columnspan=2)
        messagebox.showinfo("Erro", "Por favor, insira valores válidos para peso e altura")


frame = Frame(janela, padx= 20, pady= 40).grid(column=1, row=1)
Label(frame, text="Clique no botão para calcular seu IMC", pady=40).grid(column=1, row=1, columnspan=2)



Label(frame, text="Qual seu peso em kg?").grid(column=1, row=2)
peso = Entry(frame)
peso.grid(column=2, row=2)


Label(frame, text="Qual sua altura em metros?").grid(column=1, row=3)
altura = Entry(frame)
altura.grid(column=2, row=3)


Button(frame, text="Calcular", command=calcular_imc).grid(column=2, row=4)
resultado = Label(frame)
resultado.grid(column=1, row=5, columnspan=2)


janela.title("Calculadora de IMC")
janela.mainloop()
