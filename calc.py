numeros = []

print("insira 4 números:")

for i in range(4):
    entrada = input(f"Digite o {i+1}º número: ")
    
    numero_convertido = float(entrada)
    numeros.append(numero_convertido)

media = sum(numeros) / len(numeros)


print(f"a média dos números é: {media:.2f}")