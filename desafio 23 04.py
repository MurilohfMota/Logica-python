#Desafio: cria uma lista chamada minhaLista com os seguintes itens: 76,92.3,'oi',True, 4 , 76.
minhaLista = [76, 92.3, "oi", True, 4, 76]
# a) inserir "pitomba" e 76 no final da lista
final = ['Pitomba',76]
a = minhaLista+final
print(a)
#b) inserir o valor cibele na posição de índice 3.
inicio = minhaLista[:4]
final2 = minhaLista[4:]
cibele = ['cibele']
b = inicio[:] + cibele [:] + final2[:]
print(b)
#c) inserir o valor 99 no inicio da lista
inicio = [99]


c = b + inicio
print(c)
#d) Encontrar o índice do "oi"
if minhaLista[0] == 'oi' :
   print(f'o oi está no indice 0')
elif minhaLista[1] == 'oi' :
   print(f'o oi está no indice 1')
elif minhaLista[2] == 'oi' :
   print(f'o oi está no indice 2')
elif minhaLista[3] == 'oi' :
   print(f'o oi está no indice 3')
elif minhaLista[4] == 'oi' :
   print(f'o oi está no indice 4')
elif minhaLista[5] == 'oi' :
   print(f'o oi está no indice 5')
elif minhaLista[6] == 'oi' :
   print(f'o oi está no indice 6')
elif minhaLista[7] == 'oi' :
   print(f'o oi está no indice 7')
#e) remover True da lista
inicio = c[:3]
final =   c[4:]
e = inicio + final
print(e)
