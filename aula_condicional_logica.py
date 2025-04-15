alturaPedro = 150
idadePedro = 19

print(alturaPedro >= 165)
print('and')
print(idadePedro >= 18)
if alturaPedro >= 165 and idadePedro >= 18:
    print("aceito nas forcas armadas")
else:
    print("nao foi aceito")

if alturaPedro >= 165 or idadePedro >= 18:
    print("aceito nas forcas armadas")
else:
    print("nao foi aceito")

vLr = int(input('doido, informe o valor:...'))
print("digitado", vLr)
numero = vLr

if numero >= 20 and numero <= 90:
    print("dentro da faixa 20 e 90")
else:
    print("fora da faixa ")


