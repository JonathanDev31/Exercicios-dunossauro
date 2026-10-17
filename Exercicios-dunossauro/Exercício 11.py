#Exercício 11
#Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

#O produto do dobro do primeiro com metade do segundo .
#A soma do triplo do primeiro com o terceiro.
#O terceiro elevado ao cubo.


int1 = int(input("Digite um número inteiro: "))
int2 = int(input("Digite outro número inteiro: "))
real = float(input("Digite um número real: "))

primeiro = int1 * 2 * int2 / 2
segundo = int2 / 2
terceiro = real ** 3

soma = int1 * 3 + real

print(primeiro)
print(soma)
print(terceiro)



