frase = (input ('escreva alguma coisa meu bacano lindo: ')).strip().upper()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print ("a ultima letra A apareceu na posição {}".format(frase.rfind('A')))
