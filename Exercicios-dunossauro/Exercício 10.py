#Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

#Formula
#F = (C * 9/5) + 32

g_celcius = float(input("Digite uma temperatura em graus celcius: "))

F = (g_celcius * 9/5) + 32


print(f"São {F:.1f} Graus Fahrenheit!")