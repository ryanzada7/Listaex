numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = numeros.split()


lista_numeros = [int(numero) for numero in lista_numeros]


lista_numeros.sort()


print("A lista ordenada em ordem crescente é:", lista_numeros)
