from random import shuffle
aluno1=str(input("digite o nome do 1º aluno: "))
aluno2=str(input("digite o nome do 2º aluno: "))
aluno3=str(input("digite o nome do 3º aluno: "))
aluno4=str(input("digite o nome do 4º aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("a ordem do sorteio é: {}".format(lista))
