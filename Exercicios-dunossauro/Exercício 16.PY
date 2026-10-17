#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta 
# é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math
metros_quadrado = float(input("Digite quantos metros quadrados: "))

litros = metros_quadrado / 3
quantidades_litros_lata = 18
valor_lata = 80.00
quantidade_latas = math.ceil(litros/ quantidades_litros_lata)
preço_total = valor_lata * quantidade_latas

print(f"Você vai precisar de {quantidade_latas} latas de tintas e o valor vai ser R$ {preço_total:.2f}")