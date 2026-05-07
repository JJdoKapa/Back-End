nome = str(input('Digite algum nome: ')).strip()
dividido = nome.split()

print('Analisando seu nome...')
print('esse nome em maíusculas é: {}'.format(nome.upper()))
print('esse nome em minusculas é: {}'.format(nome.lower()))
print('esse nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('esse primeiro nome é: {} e ele tem: {} letras'.format(dividido [0], len (dividido[0])))
