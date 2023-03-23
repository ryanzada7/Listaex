numeros = input("Digite uma lista de números separados por vírgula: ").split(",")
pares = []

for numero in numeros:
    if int(numero) % 2 == 0:
        pares.append(numero)

print("Os números pares da lista são: ", ", ".join(pares))
