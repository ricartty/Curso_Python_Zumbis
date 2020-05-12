#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
preco = float(input("Insira o valor da mercadoria: "))
percent = float(input("Insira o percentual do desconto: "))
desc= (preco*percent/100)
preco = (preco - desc)
print ("O valor do desconto é de %.2f" %desc)
print ("O valor final da mercadoria é R$%.2f" %preco)

