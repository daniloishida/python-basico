#open('arquivo.txt', 'w')
# open('c:\\teste\\arquivo.txt', 'w')
# para linux não precisa de duas barras porque é para o outro lado
''' 
W = escrita (Salvar/criar arquivo) Sobrescreve
r = Leitura (Abrir um arquivo) 
r+ = Leitura e Escrita
a = append adiciona os textos abaixo dos que já existem
b = arquivos binarios, que não são textos
obs: é possivel abrir como rb ou wb e etc
'''

arquivo = open('arquivo.txt','w')
for i in range(0, 1000):
    arquivo.write(str(i)+"\n")

arquivo = open('arquivo.txt','r')
print(arquivo.read())

