#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:
gigabytes = float(input("Digite o tamanho em GB: "))

megabytes = gigabytes * 1024

print(f"O arquivo tem {megabytes} MB")
