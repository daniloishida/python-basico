nomes = ['Guilherme', 'Marcelo', 'Joao', 'Julia']

for nome in nomes:
    print(nome)

for i in range(4):
    print(nomes[i])

for i in range(len(nomes)):
    print(nomes[i])


lista_de_numeros = range(5, 11, 2)

for item in lista_de_numeros:
    print(item)

for item1 in range(0, 100, 20):
    print(item1)

palavra = 'Danilo Ishida'
x = 0

for letra in palavra:
    print(letra)

while x < 10:
    print('I ainda é menor que 10:', x)
    x = x + 1
    x -= 1
    x += 1
print('Acabou o while:',x)

lista_frutas = ['Maca','pera','Uva','Abacaxi', 'Goaiaba']
contador = 0

for fruta in lista_frutas:
    contador += 1
print('Tem',contador,'Frutas na lista.')
print('Tem',len(lista_frutas),'Frutas na lista.')

y = 0
while True:
    print(y)
    if y == 20:
        break
    y += 1

'''
Exercicio: faça um programa que leia a quantidade de pessoas que serao convidadas para uma festa
apos isso o programa ira perguntar o nome de todas as pessoas e colocar numa lista de convidados
apos isso imprimir todos os nomes da lista
'''

convidados = input('Digite quantos convidados:')
nome_convidados = [ ]
p = 1

while p <= int(convidados):
    nome_convidados.append(input('Digite o nome do convidado #'+str(p)+':'))
    p += 1

for nomi in range(len(nome_convidados)):
    print('Convidado #'+str(nomi+1)+':'+nome_convidados[nomi])