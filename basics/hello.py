# Variáveis

name = 'André'
idade = 30
print("Olá,", name, ", você tem ", idade, "anos!")
print("Seja muito bem vindo {}, espero que vc goste do programa".format(name))
print(f"ola lindão {name} vc é um gato e esse ano vai ganhar muita grana")


variavel = 5
float = 543.8
boleado = True
x = int("43") # Converte
a,b,c = 1,2,3 # multiplas atribuições

print(type(float))

print(variavel+float)
print(float-variavel)
print(float*variavel)
print(float/variavel)
print(float//variavel)

print(1==2)
print(2==2)
print(1!=2)
print(1<2)

print(True and True)
print(True or True)
print(not False)

um = 1
um += 2
print(um)


# Funções

def multiplicacao(num1, num2):
    return num1 * num2


result = multiplicacao(5, 20)

print(result)


def func():
    global y #torna a variável global, podendo ser acessada em outro lugar
    y = 3


func()

print(y)


# Lists

letters = ['a', 'b', 'c', 'd']

print(letters[0])
print(letters[-2])
print(letters[1:3])
print(letters[:3])
print(letters[2:])

letters.append('e')
print(letters)

letters.insert(2, 'q')
print(letters)

letters.remove('d')
print(letters)

letters.pop()
print(letters)

letters.pop(0)
print(letters)

numbers = [1, 2, 3]
numbers.extend(letters)
print(numbers)


# Dictionaries = coleção de itens

pessoa = {
    'name': 'Andre',
    'idade': 30
}

print(pessoa)
print(pessoa.keys())
print(pessoa.values())
print(pessoa['name'])

pessoa['nacionalidade'] = 'brasileiro'

print(pessoa['nacionalidade'])


# Condições e Loops

if variavel > um:
    print('Maior')
else:
    print('Menor')


i = 0

while i < 3:
    print(i)
    i += 1

    # if i == 1:
    #     continue
    #
    # if i == 2:
    #     break


f = 0

while f < 5:
    if f == 3:
        f += 1
        continue

    print(1/(3-f))
    f += 1


range_numbers = range(3,15)

for v in range_numbers:
    print(v)

for person in pessoa.keys():
    print(pessoa[person])


# Classes e objetos
from classess import Carro

carro1 = Carro('branco', 'toyota', 'prius')
carro2 = Carro('vermelho', 'chevrolet', 'astra')
carro3 = Carro('azul', 'volks', 'saveiro')

print(carro2.cor)
carro3.drive()
carro1.get_values()


