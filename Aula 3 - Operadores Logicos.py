var_verdade = True
# Boolean ou Bool
var_falso = False
# Boolean ou Bool
print(type(var_verdade), type(var_falso))
# se condiçao (Então é dois pontos( : ) )
'''
simbolos de comparação:
< = Menor
> = Maior 
== = Comparação
>= = Maior ou igual
<= = Menor ou igual
!= = Diferente 
and = E
or = Ou
'''
if var_verdade == True:
    print('Var_Verdade é:', var_verdade)

a = 2
b = 20
if a > b and a < 10:
    print(a, 'é maior do que', b)
else:
    print(a, 'é menor do que', b)

# if, else e elif
print('Opcoes:\n1= Escreve Guilherme\n2 = Escreve joao \n3 = Escreve maria')
opcao = input("Escolha uma opcao:")

if opcao == '1':
    print('Guilherme')
elif opcao == '2':
    print('Joao')
elif opcao == '3':
    print('Maria')
else:
    print('opcao invalida!')

# Negacao
idade = 50

if not idade == 50:
    print('Voce nao tem 50 anos!')
else:
    print('Voce tem 50 anos!')

if not True:
    print('Entrou no if')
else:
    print('Entrou no else')

''' 
Exercicio:
Faça um programa para perguntar a idade, o peso e a altura e decida se esta apta a ser do exercico
condicao: maior que 18 anos
mais ou igual 60 kg
mais ou igual 1.70m
'''

idade1 = input('Digite a sua idade:')
peso = input('Digite seu peso:')
altura = input('Digite sua altura:')

if idade1>'18' and peso >= '60' and altura >= '1.7' :
    print('Voce esta apto para o exercito!')
else:
    print('Voce não esta apto para o exercito!')