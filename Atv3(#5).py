n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua 2° nota: '))

media = (n1 + n2) / 2

if media>= 7 and media < 10:     
    print ('Você foi Aprovado!!')
elif media >= 10:
    print ('Você foi aprovado com Distinção!')    
else:
    print ('Você foi reprovado')