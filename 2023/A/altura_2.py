qtd_brinquedos, altura = input().split()
qtd_brinquedos, altura = int(qtd_brinquedos), int(altura)
alturas = input().split()

print(len(list(filter(lambda altura_brinquedo: altura >= int(altura_brinquedo), alturas))))