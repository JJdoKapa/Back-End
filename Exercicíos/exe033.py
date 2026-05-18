N1 = float(input("digite o primeiro número"))
N2 = float(input("digite o segundo número"))
N3 = float(input("digite o terceiro número"))
menor = N1
maior = N1
if N2 > N1 and N2>N3:
    maior = N2
if N3 > N1 and N3>N2:
    maior = N2
if N2 < N1 and N2>N3:
    menor = N2
if N2 < N1 and N3>N2:
    menor = N3
print('o maior número digitado foi: {}'.format(maior))
print('o menor número digitado foi: {}'.format(menor))
