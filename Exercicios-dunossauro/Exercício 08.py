#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_horas = float(input("Qual o valor em reais que você ganha por hora trabalhada?: "))
numero_horas_mes = float(input("Quantas horas você trabalha no mês?: "))

salario = valor_horas * numero_horas_mes

print(f"O salario recebido no mês é {salario:.2f}")

