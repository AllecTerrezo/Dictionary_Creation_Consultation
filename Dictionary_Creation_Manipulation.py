global L
import random
from datetime import date

def list_tuplas():
    global L
    L = {}
    for i in range(1000):
        mes = random.randint(1,12)
        if mes == 2:
            dia = random.randint(1,28)
        elif mes ==4 or mes == 6 or mes==9 or mes==11:
            dia = random.randint(1, 30)
        else:
            dia = random.randint(1,31)
        tamanho_nome = random.randint(1,10)
        s = ''
        for j in range (tamanho_nome):
            num_aleatorio = random.randint(1,2)
            if num_aleatorio == 1:
                s = chr(random.randint(65,90))+ s
            else:
                s = chr(random.randint(97,122))+ s       
        nome = s
        domain = '@xyz.com.br'
        email = (s + domain)
        tupla = email, dia, mes
        L[nome] = tupla

    print(L)
    

def aniversariante():
    global L
    niver = []
    today = date.today()
    day = today.strftime("%d")
    month = today.strftime('%m')
    day = int(day)
    month = int(month)
    for i in L:
        dia = (L[i][1])
        mes = (L[i][2])
        nome = (L[i][0])
        nome, dominio = nome.split('@')
        if dia == day and mes == month:
            niver.append(nome)
    print ('aniversariante(s) do dia: ', niver)

def main():
    list_tuplas()
    aniversariante()


main()
