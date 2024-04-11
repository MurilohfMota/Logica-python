from tkinter import *

root = Tk()
class App():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.Construtor_botões()
        self.Caixa_texto()


        root.mainloop()
        
    def tela(self) :
        self.root.title( "Exercicio 04" ) 
        self.root.configure ( background="#184e77")
        self.root.geometry ( "1250x720" )
        self.root.resizable (True, True)
        self.root.maxsize ( width = 1920, height = 1080 )
        self.root.minsize ( width = 720, height = 560 )

    def frames_da_tela(self):
        self.frame_1 = Frame (self.root, bd = 4, bg = '#d9ed92',
                            highlightbackground= '#34a0a4', highlightthickness=3 )
        self.frame_1.place(relx= 0.02 , rely=0.01, relwidth= 0.96,relheight= 0.40)
        self.frame_2 = Frame (self.root, bd = 4, bg = '#d9ed92',
                            highlightbackground= '#34a0a4', highlightthickness=3 )
        self.frame_2.place(relx= 0.02 , rely=0.44, relwidth= 0.96,relheight= 0.40)
    #construtor de botões
    def Construtor_botões(self):
        #botâo de executar
        self.bt_executar = Button(self.frame_1, text = 'Executar')
        self.bt_executar.place ( relx = 0.9, rely = 0.85, relwidth = 0.1, relheight = 0.15)
        #botão proximo
        self.bt_proximo = Button(self.root, text = 'Proximo')
        self.bt_proximo.place ( relx = 0.89, rely = 0.87, relwidth = 0.09, relheight = 0.08)
        #botão sair
        self.bt_proximo = Button(self.root, text = 'Sair')
        self.bt_proximo.place ( relx = 0.02, rely = 0.87, relwidth = 0.09, relheight = 0.08)
    
    def Caixa_texto(self) :
        #texto de instrução da primeira tela
        self.texto = Label(self.frame_1, text = "Informe dois números inteiros e um número real.", background = '#d9ed92')
        self.texto.place ( relx = 0.0, rely = 0.010, relwidth = 0.3, relheight = 0.1 )
        #texto numero 1
        self.texto01 = Label(self.frame_1, text = "Valor inteiro", background = '#d9ed92')
        self.texto01.place ( relx = 0.3, rely = 0.010, relwidth = 0.3, relheight = 0.1 )
        #texto numero 2
        self.texto02 = Label(self.frame_1, text = "Valor inteiro", background = '#d9ed92')
        self.texto02.place ( relx = 0.5, rely = 0.010, relwidth = 0.3, relheight = 0.1 )
        #texto numero 3
        self.texto03 = Label(self.frame_1, text = "Valor real", background = '#d9ed92')
        self.texto03.place ( relx = 0.7, rely = 0.010, relwidth = 0.3, relheight = 0.1 )











home_sreen = App()
home_sreen()