frase = 'Oi, tudo bem?'
print(frase)
print(frase[0])
print(frase[1])
print(frase[0:5])
print(frase[3:10]) # imprime do 3 ao 10 caracter
print(frase[0:12:2]) # imprime e pula de 2 em 2 caracteres
print(frase[::-1]) # imprime ao inverso

lista_nomes = ['Joao', 'Maria', 'Guilherme', 'Diego', 10, 10.2]
print(type(lista_nomes))

lista_nomes.append('Geralda') # Adiciona um nome no final da lista
lista_nomes.append('Lorena')
lista_nomes.remove('Joao') # Remove o nome
lista_nomes.insert(1, 'Creosvaldo') # Adiciona um nome na posição indicada
lista_nomes [0] = 'Robervania' # Altera o nome na posição indicada

print(lista_nomes)
print(lista_nomes[0])
print(lista_nomes[4])
print(lista_nomes[0:3])
print(lista_nomes[-2])
print(lista_nomes[-1:-7:-1])

print(len(frase))# conta o numero de caracteres
print(len(lista_nomes))# conta o numero de itens

print(lista_nomes)
print(lista_nomes.pop())# Retira o ultimo nome da lista
print(lista_nomes)

frase_separada = frase.split(',')
print(frase_separada[1])
print(frase_separada[0])

frase_nova = frase + "Como vai voce?"
print(frase_nova)

lista_nomes.clear()
