#Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

print("Digite um número para ver sua tabuada.")
n = int(input())
print("TABUADA DO ",n,":")
for i in range(1,10):
    print(n,"x",i,"=",(n*i))

