#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input("Digite o tamanho de um arquivo para download (em MB): "))
link_de_internet = float(input("Digite a velocidade de um link de internet (em Mbps): "))

megabits = arquivo * 8
tempo_segundos = megabits / link_de_internet
tempo_minutos = tempo_segundos / 60

print(f"Demora mais ou menos {tempo_minutos:.2f} minutos")