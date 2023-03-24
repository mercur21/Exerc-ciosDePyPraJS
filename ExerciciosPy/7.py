#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

print("Informe dois números inteiros. ")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
while n1 != n2:
    if n1 >= n2:
        n2 += 1
        print(n2)
    if n2 >= n1:
        n1 += 1
        print(n1)