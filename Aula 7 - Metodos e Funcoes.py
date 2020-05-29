# Def é utilizado para criar funçoes
def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp


def imprime_oi():
    print('oi')


def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False


imprime_oi()
retorno = soma(75, 1289)
print(retorno)

print(tem_sete_itens("oi pessoal"))
print(tem_sete_itens("1234567"))

if tem_sete_itens([1, 2, 3, 4, 5, 6, 7]):
    print('Realmente tem 7 letras')

'''
Escreva uma funcao que recebe um objeto de coleção e retorna o valor do maior numero dentro dessa coleção
faça outra que retorna o menor numero também
'''

def maior(colecao):
    maior = colecao[0]
    for item in colecao:
        if maior<item:
            maior = item
    return maior

def menor(colecao):
    menor = colecao[0]
    for item in colecao:
        if menor>item:
            menor = item
    return menor

print(maior([1,31,14,15,77,23,88,98,1234]))
print(menor([1,31,14,15,77,23,88,98,1234]))