#desafio 1
valor = float(input('informe o valor do seu veículo. '))
ano = int(input('informe o ano do seu veiculo. '))

if ( ano < 1990 ):
    taxa = 0.01
else :
    taxa = 0.015

imposto = taxa*valor
print ( f'O valor a ser pago é R${imposto:.2f}.' )


#desafio 2
cargo = str ( input( f'Ex: \"Gerente\"\nDigite seu cargo: ' ) )
salario = float ( input ( 'informe seu salario: ' ) )

if cargo == "Gerente" or cargo == "gerente" :
    salario = salario+(salario*0.1)

elif cargo == "Engenheiro" or cargo == "engenheiro" :
    salario = salario+(salario*0.2)   

elif cargo == "Técnico" or cargo == "técnico" :
    salario = salario+(salario*0.3)
   
else : 
    salario = salario+(salario*0.4)
    
print( f'Seu novo salário será R${salario:.2f}' )