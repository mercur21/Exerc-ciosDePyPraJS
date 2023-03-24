#Exemplo:
numero = int(input("Fatorial de: ") ) #esse pede o numero

resultado=1 #recebera os valores de count que sera incrementado por o count
count=1 #contador

while count <= numero: #cria o loop
    resultado *= count #faz a multiplicação
    count += 1 #incrementa

print(resultado) #printa o resultado com os valores recebidos de count