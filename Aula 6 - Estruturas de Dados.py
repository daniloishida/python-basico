minha_lista = ['Gui', 'Joao'] # LISTA (list) (da para expandir o quanto quiser) (Dinamico)
minha_tupla = ('Guilherme', 'Pedro') # Tupla (tuple) (tem só a quantidade de array que for instanciado na variavel)
meu_dicionario = {'nome': 'Danilo', 'idade': 28} # Hashmap ou Hashtable (dict)
meu_conjunto = {'Danilo', 'Pedro', 'Thiago'} # Nao é ordenado, nao tem indice (set)

lista = []
tupla = ()
dicionario = {}
conjunto = set()

if 'Gui' in minha_lista:
    print('Gui Está na lista')

if 'Gui' in minha_tupla:
    print('Gui Está na Tupla')

if 'Gui' in meu_conjunto:
    print('Gui Está no conjunto')

print(meu_dicionario['nome'])
print(meu_dicionario['idade'])
print(len(meu_dicionario))

meu_dicionario['endereco'] = 'Rua B'
meu_dicionario['telefone'] = '888999'

if 'Danilo' in meu_dicionario.values():
    print('Danilo esta no dicionario.')

#keys = chaves (Nome) Values = Valores (Danilo)
for valores in meu_dicionario.values():
    print(valores)

for valores in meu_dicionario.keys():
    print(valores)

meu_conjunto.add('Maria')
meu_conjunto.add('Pedro') #Adicionar um dado repetido não aparece duplicado na lista
print(meu_conjunto)

if 'Pedro' in meu_conjunto:
    print('Pedro foi encontrado no conjunto')

meu_conjunto.remove('Pedro')
print(meu_conjunto)

loucura = [(1,2), (3,4), (5,6), ({'joao', 'maria'},{'gabriel'})]
print(loucura)