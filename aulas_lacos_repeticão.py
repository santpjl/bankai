#Laços de Repetição
#Usando o Laço While


#Exercício: Faça um laço de repetição While que mostre os valores de 8 a 12 

contador = 8
while contador < 12:
    print("valor", contador)
    contador = contador + 1

print("acabou")




j = 19
while j >= 14:
    print("valor de j:", j)
    j = j - 1

print("acabou")





#exercício: Usando o for, mostre todos os valores pares entre 0 e 10 
for z in range(10):
    print("valor de z:", z)
    


for b in range(11):
    if b % 2 == 0 :
        print(b , "é par")
