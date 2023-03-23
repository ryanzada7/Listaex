numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = numeros.split()

lista_numeros = [int(numero) for numero in lista_numeros]

maximo = max(lista_numeros)
minimo = min(lista_numeros)


print("O número máximo da lista é:", maximo)
print("O número mínimo da lista é:", minimo)
