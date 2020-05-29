import sys
#Por ter espaço no nome do arquivo não funciona no prompt, rodar a aula8teste.py para conseguir executar

argumentos = sys.argv #arg1 method // arg 2 - n1 // arg3 - n2

def soma(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

if argumentos[1] == "soma":
   resp = soma(float(argumentos[2]),float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]),float(argumentos[3]))

print(resp)