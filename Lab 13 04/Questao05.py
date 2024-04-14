from tkinter import *

root = Tk()
label_var = StringVar()
label_var2 = StringVar()
class App() :
    #Definir janelas, telas e frames do front
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.Botoes()
        self.Caixa_texto()
        self.Widgets()

        root.mainloop()
    #Definir e configurar telas
    def tela(self) :
        self.root.title( "Lab 13/04 questão 05" ) 
        self.root.configure ( background="#184e77")
        self.root.geometry ( "1250x720" )
        self.root.resizable (True, True)
        self.root.maxsize ( width = 1920, height = 1080 )
        self.root.minsize ( width = 720, height = 560 )
    #Definir e configurar frames e setores da tela
    def frames_da_tela(self):
        self.frame_1 = Frame (self.root, bd = 4, bg = '#d9ed92',
                            highlightbackground= '#34a0a4', highlightthickness=3 )
        self.frame_1.place(relx= 0.02 , rely=0.01, relwidth= 0.96,relheight= 0.40)
        self.frame_2 = Frame (self.root, bd = 4, bg = '#d9ed92',
                            highlightbackground= '#34a0a4', highlightthickness=3 )
        self.frame_2.place(relx= 0.02 , rely=0.44, relwidth= 0.96,relheight= 0.40)
    #
    def Botoes(self):
        #botâo de executar
        self.bt_executar = Button(self.frame_1, text = 'Executar', bd = 2 , bg = '#184e77', fg = '#d9ed92', font = ('firacode', 12), command = self.Executar)
        self.bt_executar.place ( relx = 0.9, rely = 0.85, relwidth = 0.1, relheight = 0.15)

        #botão sair
        self.bt_proximo = Button(self.root, text = 'Sair', bd = 2 , bg = '#99d98c', fg = '#184e77', font = ('firacode', 12), command = root.destroy)
        self.bt_proximo.place ( relx = 0.02, rely = 0.87, relwidth = 0.1, relheight = 0.07)
    
    def Caixa_texto(self) :
        #texto de instrução da primeira tela
        self.texto = Label(self.frame_1, text = f"Informe três números.\n Por favor preencha todos os Campos\n OBS: use \".\" para separar as casas decimais", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto.place ( relx = 0.0, rely = 0.010, relwidth = 0.3, relheight = 0.24 )
        #texto numero 1
        self.texto01 = Label(self.frame_1, text = "Primeiro número", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto01.place ( relx = 0.3, rely = 0.010, relwidth = 0.3, relheight = 0.1 )
        #texto numero 2
        self.texto02 = Label(self.frame_1, text = "Segundo número", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto02.place ( relx = 0.5, rely = 0.010, relwidth = 0.3, relheight = 0.1 )
        #texto numero 3
        self.texto03 = Label(self.frame_1, text = "Terceiro número", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto03.place ( relx = 0.7, rely = 0.010, relwidth = 0.3, relheight = 0.1,  )

        #caixa de texto do resultado no frame_2
        self.texto_resultado = Label(self.frame_2, text = "", font = ('Firacode', 16), background = '#d9ed92', textvariable= label_var)
        self.texto_resultado.place ( relx = 0.0, rely = 0.010, relwidth = 0.9, relheight = 0.9 )
    def Widgets(self) : 
        #criando campos de entrada de texto do usuario
        #campo valor inteiro 01
        self.entrada01 = Entry(self.frame_1)
        self.entrada01.place ( relx = 0.40, rely = 0.10, relwidth = 0.1, relheight = 0.1 )

        #campo valor inteiro 02
        self.entrada02 = Entry(self.frame_1)
        self.entrada02.place ( relx = 0.60, rely = 0.10, relwidth = 0.1, relheight = 0.1 )

        #campo valor inteiro 03
        self.entrada03 = Entry(self.frame_1)
        self.entrada03.place ( relx = 0.80, rely = 0.10, relwidth = 0.1, relheight = 0.1 )
    #Definir  funcções do back
    def Executar(self) : 
    #questão 5)
        self.num01 = float (self.entrada01.get())
        self.num02 = float (self.entrada02.get())
        self.num03 = float (self.entrada03.get())
        self.maiornum = 0 
        self.igual1 = FALSE
        self.igual2 = FALSE
        #primeira etapa, definir o maior numero entre o numero 1 e o numero 2
        if self.num01 > self.num02 : 
            self.maiornum = self.num01
        
        elif self.num01 < self.num02 : 
            self.maiornum = self.num02

        elif self.num01 == self.num02 : #se num01 e num02 não são maiores ou menores entre si, então eles são iguais. logo vou usar qualquer um deles
            self.maiornum = self.num01
            self.igual1 = TRUE
        #segunda etapa, definir o maior numero entre o maior numero atual e o numero 3

        if self.maiornum > self.num03 :
            label_var.set(f'{self.maiornum} é o maior número!')

        elif self.maiornum < self.num03 :
            self.maiornum = self.num03
            label_var.set(f'{self.maiornum} é o maior número!')

        elif self.maiornum == self.num03 :
            self.igual2 = TRUE
            if self.igual1 == TRUE :
                label_var.set(f'os três números são iguais')
            else :
                label_var.set(f'{self.maiornum} é o maior número!')
            

           
        





home_sreen = App()
home_sreen()