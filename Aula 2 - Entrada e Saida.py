print('hello world!\nnova linha \t tab para espaçamento ')
print('segundo print')
nome = 'Guilherme Roberto Soares'
# \n pula a linha \t da um TAB no texto
idade = 27
# Int
salario = 3000.50
# Float
tipo_idade = type(idade)
tipo_salario = type(salario)

print(nome)
print(type(nome))
# mostra o tipo do nome
print(idade)
print(tipo_idade)
# atribui a uma variavel o tipo
print(salario)
print(tipo_salario)

# Concatenação é feito com , ou +
print(nome, 'tem', idade, 'anos e', salario, 'de salario.')
print(nome + ' tem ' + str(idade) + ' anos e ' + str(salario) + ' de salario.')
# com virgula não precisa converter os numeros para strings e nem colocar espaços
nome_novo = input('Escreva seu nome: ')
# entrada de dados
idade_novo = input('Escreva sua idade:')
altura_novo = input('Escreva sua altura:')
print(nome_novo + ' tem ' + str(idade_novo) + ' anos e ' + str(altura_novo) + ' de altura.')
print(type(nome_novo), type(idade_novo), type(altura_novo))
# todos os tipos vão vir como string pois está tudo convertio já
numero1 = 10
numero2 = 53
numero3 = 7.3
resultado = ((numero1**2) + numero2) / numero3
# elevar a potencia é **
print(resultado)

