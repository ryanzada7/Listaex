numeros = input("Digite uma lista de números separados por vírgula: ")
numeros = [int(x) for x in numeros.split(",")]

numeros.sort(reverse=True)

print("Lista em ordem decrescente:", numeros)
