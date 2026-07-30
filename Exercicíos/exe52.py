maior = 0
menor = 0
for c in range(1,6):
    p = float(input(f'pesoda {c} pessoa em kg: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(f'o maior peso lido foi {maior}kg')
print(f'o menor peso lido foi {menor}kg')
