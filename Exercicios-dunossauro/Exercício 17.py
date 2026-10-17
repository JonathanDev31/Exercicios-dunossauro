#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
tamanho_metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

cobertura_tinta = tamanho_metros_quadrados / 6

preco_lata = 80

preco_galao = 25

litros_lata = 18

litros_galao = 3.6

litros_com_folga = cobertura_tinta * 1.10

latas_18 = math.ceil(litros_com_folga / 18)

galao_3_6 = math.ceil (litros_com_folga / 3.6)

custo_latas_18 = latas_18 * preco_lata

custo_galao_3_6 = galao_3_6 * preco_galao

latas_mix = litros_com_folga // litros_lata

litros_restantes = litros_com_folga - (latas_mix * litros_lata)

galoes_mix = math.ceil(litros_restantes / litros_galao)

custo_mix = (latas_mix * preco_lata) + (galoes_mix * preco_galao ) 

print(f"O valor total das LATAS ficam R$ {custo_latas_18:.2f}")

print(f"O valor total dos GALOES ficam R$ {custo_galao_3_6:.2f} ")

print(f"Na mistura, USE {int(latas_mix)} lata(s) de 18L e {galoes_mix} galão(ôes) de 3.6L, total R$ {custo_mix:.2f}")
