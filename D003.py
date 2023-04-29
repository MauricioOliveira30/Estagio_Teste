def inveterte_palavra(palavra):

    nova_palavra=""

    for i in range(len(palavra) - 1, -1, -1):
        nova_palavra += palavra[i]
    return nova_palavra
palavra_original=str(input("Digite uma palavra:"))
palavra_invertida=inveterte_palavra(palavra_original)
print(palavra_invertida)