import tkinter as tk

def calcular_media():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    num3 = float(entry_num3.get())
    media = (num1 + num2 + num3) / 3
    label_resultado.config(text="Média: {:.2f}".format(media))

# Cria uma janela
window = tk.Tk()
window.title("Cálculo da Média")

# Cria os rótulos e campos de entrada
label_num1 = tk.Label(window, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

label_num3 = tk.Label(window, text="Número 3:")
label_num3.pack()
entry_num3 = tk.Entry(window)
entry_num3.pack()

# Botão para calcular a média
button_calcular = tk.Button(window, text="Calcular Média", command=calcular_media)
button_calcular.pack()

# Rótulo para exibir o resultado
label_resultado = tk.Label(window, text="Média: ")
label_resultado.pack()

# Inicia o loop principal da janela
window.mainloop()
