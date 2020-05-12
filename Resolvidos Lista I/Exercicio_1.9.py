#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km roda
kmp = float(input("Quantidade de km percorridos: "))
dias = float(input ("Quantos dias de aluguel: "))
preco = 60*dias + 0.15*kmp
print ("O valor final do aluguel é de %.2f" %preco)

