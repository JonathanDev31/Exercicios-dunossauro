#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
temperatura_fahrenheit = float(input("Digite um valor em temperatura em fahrenheit: "))

celsius = 5 * ((temperatura_fahrenheit - 32) / 9)

print(f"A temperatura em graus celcius é {celsius:.2f}")