#Escreva um programa para calcular a redu��o do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele j� fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perder�. Exiba o total de dias.
qtd_cig = int(input("Quantos cigarros vc fuma por dia? "))
ano_cig = int(input("Quantos anos vc j� fumou "))
total_cigarros = ano_cig * 365 * qtd_cig
dias_perdidos = total_cigarros / 144
print ('Voc� perdeu aproximadamente %.2f dias' %dias_perdidos)
