valor = none # valor nulo NULL

numero = int( input('Digite um valor' ) )
i = 0
for i in range(numero):
    print(i)
    
for i in range(2,8):
    print(i)


for i in range(1,11):
    if i % 2 == 0:
        print(f'O numero {i} eh par')
    else:
        print(f'O numero {i} eh impar')

notas = [10,8] #criando uma lista
soma = 0

for nota in notas: #variavel nota pode ser criada na hora
    soma += nota

print('A soma vale ', soma)
