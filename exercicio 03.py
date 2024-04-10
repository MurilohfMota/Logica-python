

#exercicio 03
num01 = input ( 'Informe um número: ')

print ( 'O número que informado foi' ,num01)
#_____________________________________________________________________
#exercicio 04

num01 = int(input('informe o primeiro numero: '))
num02 = int(input('informe o segundo numero: '))

print('A soma dos numeros informados é ',(num01+num02))
#_____________________________________________________________________
#exercicio 05

num01 = int(input('informe a nota do primeiro trimestre: '))
num02 = int(input('informe a nota do segundo trimestre: '))
num03 = int(input('informe a nota do terceiro trimestre: '))
#float num04 = input("teste")
media = float(((num01+num02+num03)/3))
print ( f'A sua média anual é {media:.2f}')
#__________________________________________________________________________
#exercicio 06

sal = float(input('Quanto você ganha por hora? '))
horas = float(input('Quantas horas trabalhadas no mês? '))
salario = sal * horas
print ( f'Seu salário esperado é R$ {salario:.2f}' )
#_____________________________________________________________-
#exercicio 05 - desafio 

#recebe o peso calculado
peso = int(input('Qual o peso dos pexes em kg?'))
#verificar se o peso ultrapassar o limite
if peso > 50:
    #se sim, calcular quanto de multa será gerada pro peso pescado.
    multa = float((peso - 50) * 4)
    print (f'a Multa esperada é R${multa:.2f}')
else :
    #caso não ultrapasse, não será cobrado multa.
    print ( 'Não será cobrado multa!' )