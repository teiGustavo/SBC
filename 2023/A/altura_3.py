qtd_brinquedos, altura = input().split()
qtd_brinquedos, altura = int(qtd_brinquedos), int(altura)
alturas = input().split()

alt = [altura_minima for altura_minima in alturas if int(altura_minima) <= altura]

print(len(alt))