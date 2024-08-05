qtd = 0

qtd_brinquedos, altura = input().split()
qtd_brinquedos, altura = int(qtd_brinquedos), int(altura)
alturas = input().split()

for i in range(qtd_brinquedos):
    if altura >= int(alturas[i]):
        qtd += 1

print(qtd)