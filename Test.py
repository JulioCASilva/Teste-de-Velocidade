from re import X
import time

print('Olá mundo')  #imprimir na tela (Olá mundo)
print('Iniciando contagem:') 
for n in range(1, 1001):
 print(n, end=' ')  #Contagem de numeros de 1 até 1000

#inicio do contador de tempo de duração
inicio = time.time()
x = 0

while x < 100000000:
 x = x + 1

fim = time.time()
total = fim - inicio
#fim do contador

print("Tempo total: " + str(total))  #imprimir o resultado da contagem

