#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
d = float(input("Qual a distância da viagem em km ?: "))
vm = float(input("Qua a velocidade média da viagem km/h?:"))
t = (d/vm)
print ("O tempo médio da viagem é %.1f " %t)