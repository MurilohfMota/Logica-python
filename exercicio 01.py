


class Pessoa:
    nome = 'murilo'
    idade = 25
    altura = 1.70
    dev = True

Pessoa01 = Pessoa
Pessoa02 = Pessoa
Pessoa02.idade = 28
Pessoa02.nome = 'Pedro'
Pessoa02.altura = 1,80
Pessoa02.dev = False


idade1 = 25
idade2 = 28
print(Pessoa01.idade + Pessoa02.idade)

print(idade1*idade2)

print(idade1/idade2)

print(idade1**idade2)

print(idade1//idade2)

print(idade1%idade2)

print(idade1**idade2)

print ( 2 * idade1 + idade2 * 3 / 4)


