from tkinter import *

root = Tk()
label_var = StringVar()
class App() :
    #Definir telas e frames do front
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.Construtor_botões()
        self.Caixa_texto()
        self.Widgets()

        root.mainloop()
        
    def tela(self) :
        self.root.title( "Lab 13/04 questão 04" ) 
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
        self.bt_executar = Button(self.frame_1, text = 'Executar', bd = 2 , bg = '#184e77', fg = '#d9ed92', font = ('firacode', 12), command = self.Executar)
        self.bt_executar.place ( relx = 0.9, rely = 0.85, relwidth = 0.1, relheight = 0.15)

        #botão sair
        self.bt_proximo = Button(self.root, text = 'Sair', bd = 2 , bg = '#99d98c', fg = '#184e77', font = ('firacode', 12), command = root.destroy)
        self.bt_proximo.place ( relx = 0.02, rely = 0.87, relwidth = 0.1, relheight = 0.07)
    
    def Caixa_texto(self) :
        #texto de instrução da primeira tela
        self.texto = Label(self.frame_1, text = f"Informe suas notas.\n Por favor preencha todos os Campos.\n OBS: use \".\" para separar as casas decimais", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto.place ( relx = 0.0, rely = 0.010, relwidth = 0.3, relheight = 0.24 )
        #texto numero 1
        self.texto01 = Label(self.frame_1, text = "Primeira nota", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto01.place ( relx = 0.3, rely = 0.010, relwidth = 0.3, relheight = 0.1 )
        #texto numero 2
        self.texto02 = Label(self.frame_1, text = "Segunda nota", background = '#d9ed92', fg = '#184e77', font = ('firacode', 12))
        self.texto02.place ( relx = 0.5, rely = 0.010, relwidth = 0.3, relheight = 0.1 )
        

        #caixa de texto do resultado no frame_2
        self.texto_resultado = Label(self.frame_2, text = "", background = '#d9ed92', textvariable= label_var)
        self.texto_resultado.place ( relx = 0.0, rely = 0.010, relwidth = 0.9, relheight = 0.9 )
    def Widgets(self) : 
        #criando campos de entrada de texto do usuario
        #campo valor inteiro 01
        self.entrada01 = Entry(self.frame_1)
        self.entrada01.place ( relx = 0.40, rely = 0.10, relwidth = 0.1, relheight = 0.1 )

        #campo valor inteiro 02
        self.entrada02 = Entry(self.frame_1)
        self.entrada02.place ( relx = 0.60, rely = 0.10, relwidth = 0.1, relheight = 0.1 )

    #Definir  funcções do back
    def Executar(self) : 
        #calculo questão 02
        self.nota01 = float (self.entrada01.get())
        self.nota02 = float (self.entrada02.get())
            

        #questão 4)
        self.resultado = ((self.nota01 + self.nota02)/2)
        if self.resultado >= 7 : 
            label_var.set(f'Parabens você foi Aprovado!')
        else : 
            label_var.set(f'Infelizmente você foi Reprovado')
        





home_sreen = App()
home_sreen()