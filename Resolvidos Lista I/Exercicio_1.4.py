#Fa�a um programa que calcule o aumento de um sal�rio. Ele deve solicitar o valor do sal�rio e a porcentagem do aumento. Exiba o valor do aumento e do novo sal�rio.
salario = float(input("Insira o valor do sal�rio: "))
percent = float(input("Insira o percentual de aumento: "))
aumento = (salario*percent/100) 
salario = (salario+aumento)
print ("O aumento do s�lario � de R$ %.2f" %aumento)
print ("O novo sal�rio � R$ %.2f" %salario)
