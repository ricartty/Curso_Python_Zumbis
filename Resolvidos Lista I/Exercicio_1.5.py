#Solicite o pre�o de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o pre�o a pagar.
preco = float(input("Insira o valor da mercadoria: "))
percent = float(input("Insira o percentual do desconto: "))
desc= (preco*percent/100)
preco = (preco - desc)
print ("O valor do desconto � de %.2f" %desc)
print ("O valor final da mercadoria � R$%.2f" %preco)

