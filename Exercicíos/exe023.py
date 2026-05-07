numero = int(input('informe um número de 0 até 9999: '))
U = numero//1 % 10
D = numero//10 % 10
C = numero//100 % 10
M = numero//1000 % 10
print('analisando {}'. format(numero))
print('unidade {}'. format(U))
print('dezena {}'. format(D))
print('centena {}'. format(C))
print('milhar {}'. format(M))
