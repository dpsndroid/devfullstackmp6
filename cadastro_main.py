import tkinter

janela = tkinter.Tk()
janela.geometry("500x300")
janela.title("SISTEMA DE CADASTRO")


#etiqueta e caixa de entrada mod1
mod1 = tkinter.Label(master = janela, text = "Modelo 1:")
mod1.place(x=20,y=10)

mod2 = tkinter.Entry(janela)
mod2.place(x=20,y=30)

#etiqueta e caixa de entrada mod3
mod3 = tkinter.Label(master = janela, text = "Modelo 3:")
mod3.place(x=20,y=60)

mod4 = tkinter.Entry(janela)
mod4.place(x=20,y=80)


#botao
botao = tkinter.Button(master = janela, text = "Botão",)
botao.place(x=20,y=150)

janela.mainloop()
