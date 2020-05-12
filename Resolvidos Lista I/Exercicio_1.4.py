#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Insira o valor do salário: "))
percent = float(input("Insira o percentual de aumento: "))
aumento = (salario*percent/100) 
salario = (salario+aumento)
print ("O aumento do sálario é de R$ %.2f" %aumento)
print ("O novo salário é R$ %.2f" %salario)
