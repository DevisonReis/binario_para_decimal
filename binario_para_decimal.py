binario = int(input('Informe um número binário: '))

bina = binario
decimal, i = 0, 0

while binario != 0:
    resto = binario % 10
    decimal = decimal + resto * pow(2, i)
    binario = binario // 10
    i += 1

print(f'O número {bina} em binário equivale a {decimal} em decimal')
