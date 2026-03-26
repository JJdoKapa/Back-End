dias = float (input("informe quantos dias o carro está com o carro?: "))
km = float (input("quantos km você rodou com o carro?: "))
diarias = dias*60
percurso = km*0.15
custo = diarias + percurso
print("o total a pagar é de R$: {:.2f}".format(custo))
