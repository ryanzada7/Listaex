numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = numeros.split()

lista_numeros = [int(numero) for numero in lista_numeros]
media = sum(lista_numeros) / len(lista_numeros)

print("A média dos números na lista é:", media)
