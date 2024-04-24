#lista com 3 elementos


Dias = [ 3 , 1 , 10 ]
lista = 'string'
#printando a lista completa
print(f'{Dias}')


print('---------------------------------------------------------------------------------------')
#Mudando valores de indices na lista
z = [ 3 , 8 , 9]
z[0] = 7
print(f'{z}')


print('---------------------------------------------------------------------------------------')
#criando ponteiros
V = [6,7,5,8,9]
L = V
#verificando o ponteiro
print(L == V)
print(L is V)
print(L[0] is V[0])
L[0] = 5
print(L[0] is V[0])
print(L)
print(V)


print('---------------------------------------------------------------------------------------')
#criando um clone de uma lista
a = [81,82,83]
b = a[:]
#verificando e comparando os valores entre os objetos e os objetos


print(a == b)
print(a is b)
print(a[0] is b[0])
b[0] = 5
print(a[0] is b[0])
print(a)
print(b)
print('---------------------------------------------------------------------------------------')
#apredendo como manipular partes e intervalos personalizados da lista
caracteres = ['a','b','c','d','e','f']
print(caracteres[1:3])
print(caracteres[:4])
print(caracteres[3:])
print(caracteres[:])
print('---------------------------------------------------------------------------------------')
#teste inserir indices na lista
caracteres.insert(7,'g')
print(caracteres)
print('---------------------------------------------------------------------------------------')


a = [1 , 2 , 3]
b = a[:]
b[0] = 5
print(a[3])