preco = float(input("digite o preço do prouto: "))
desconto = preco - (preco*5/100)
print("o produto estava: {:.0f}$. Mas com o desconto de 5% ele está por: {:.0f}$". format(preco, desconto))
