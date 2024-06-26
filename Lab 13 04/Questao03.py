from tkinter import *

root = Tk()
label_var = StringVar()
class App() :
    #Definir telas e frames do front
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.Caixa_texto()
        self.Widgets()

        root.mainloop()
        
    def tela(self) :
        self.root.title( "Lab 13/04 questão 03" ) 
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
    def botoes(self):
        #botâo de executar
        self.bt_executar = Button(self.frame_1, text = 'Executar', bd = 2 , bg = '#184e77', fg = '#d9ed92', font = ('firacode', 12), command = self.Executar)
        self.bt_executar.place ( relx = 0.9, rely = 0.85, relwidth = 0.1, relheight = 0.15)

        #botão sair
        self.bt_proximo = Button(self.root, text = 'Sair', bd = 2 , bg = '#99d98c', fg = '#184e77', font = ('firacode', 12), command = root.destroy)
        self.bt_proximo.place ( relx = 0.02, rely = 0.87, relwidth = 0.1, relheight = 0.07)
    
    def Caixa_texto(self) :
        #texto de instrução da primeira tela
        self.texto = Label(self.frame_1, text = f"Informe um número.\n Por favor preencha todos os Campos", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto.place ( relx = 0.0, rely = 0.010, relwidth = 0.3, relheight = 0.17 )
        #texto numero 1
        self.texto01 = Label(self.frame_1, text = "Digite um número", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto01.place ( relx = 0.3, rely = 0.010, relwidth = 0.3, relheight = 0.1 )
        
        

        #caixa de texto do resultado no frame_2
        self.texto_resultado = Label(self.frame_2, text = "", font = ('Firacode', 16), background = '#d9ed92', textvariable= label_var)
        self.texto_resultado.place ( relx = 0.0, rely = 0.010, relwidth = 0.9, relheight = 0.9 )
    def Widgets(self) : 
        #criando campos de entrada de texto do usuario
        #campo valor inteiro 01
        self.entrada01 = Entry(self.frame_1)
        self.entrada01.place ( relx = 0.40, rely = 0.10, relwidth = 0.1, relheight = 0.1 )

    #Definir  funcções do back
    def Executar(self) : 
        #calculo questão 03
        self.int01 = int (self.entrada01.get())
        
            

        #questão 3)
        if self.int01 > 0 :
            label_var.set(f'{self.int01} é positivo')
        elif self.int01 < 0 :
            label_var.set(f'{self.int01} é negativo')
        else :
            label_var.set(f'{self.int01} é neutro')
        





home_sreen = App()
home_sreen()