#João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos
# além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peixes = float(input("Digire quantos Quilos de peixe João Pescou: "))

if peixes > 50:
    excedido = peixes - 50 
    multa = 4 * excedido
    print(f"João pescou {peixes} Quilos de peixes, excedeu o limite maximo de (50 Quilos) sendo {excedido} quilos de peixes a mais e ira pagar R$ 4,00 reais por quilos excedentes sendo o valor total R$ {multa:.2f}")
else:
    print(f"João pescou {peixes} Quilos de peixes")
