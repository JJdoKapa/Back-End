print('-=-' * 10)
print('analisador de triângulos')
print('-=-' * 10)
a = float(input('primeiro segmento'))
b = float(input('segundo segmento'))
c = float(input('terceiro segmento'))
if a<b+c and b<a+c and c<a+b:
    print('os segmentos acima podem formar um triângulo')
else:
    print('os segmentos acima não podem formar um trângulo')
