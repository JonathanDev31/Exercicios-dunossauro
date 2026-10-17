#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o lado do quadrado: "))
area = lado * lado
dobro_area = area * 2

print(f"O dobro da área é {dobro_area:.2f}")