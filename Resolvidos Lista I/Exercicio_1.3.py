#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = float(input("Insira a quantidade em DIAS: "))
dias = (dias * 86400)
horas = float(input("Insira a quantidade em HORAS: "))
horas = (horas * 3600)
minutos = float(input("Insira a quatidade em MIUTOS: "))
minutos = (minutos * 60)
segundos = float(input ("Inria a quantidade em SEGUNDOS"))
resultado = (dias + horas + minutos + segundos)

print ("O resultado total em segundos é %.2f " %resultado)