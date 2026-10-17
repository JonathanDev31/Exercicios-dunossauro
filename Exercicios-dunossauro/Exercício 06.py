#Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
import math

raio = float(input("Digite o raio de um circulo: "))

area = raio * raio * (math.pi)

print(f"O valor da área é {area:.2f}")