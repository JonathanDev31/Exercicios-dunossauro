#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$


valor_hora = float(input("Digite quantos reais você ganha por hora trabalhadas: "))
hora_trabalhada = float(input("Digite quantas horas você trabalha no mês: "))

salario_bruto_mensal = valor_hora * hora_trabalhada
imposto_de_renda = salario_bruto_mensal * 0.11
inss = salario_bruto_mensal * 0.08
sindicato = salario_bruto_mensal * 0.05
salario_liquido = salario_bruto_mensal - imposto_de_renda - inss - sindicato
print(f"Salario Bruto : R$ {salario_bruto_mensal:.2f}")
print(f"IR (11%) : R$ {imposto_de_renda:.2f}")
print(f"INSS (8%) : R$ {inss:.2f}")
print(f"Sindicato (5%) : R$ {sindicato:.2f}")
print(f"Salário liquido : R$ {salario_liquido:.2f}")