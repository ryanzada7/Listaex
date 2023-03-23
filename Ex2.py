palavras = input("Digite uma lista de palavras separadas por espaço: ")
lista_palavras = palavras.split()

for palavra in lista_palavras:
    if palavra.startswith("a") or palavra.startswith("A"):
        print(palavra)