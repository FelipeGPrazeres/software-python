import random
listaNumeros = [random.randint(1,100) for _ in range(5)]

def main():
#adicionar a lista
    def adicionarLista(lista):
        return listaNumeros.append(numeroAdd)
#remover da lista
    def removerLista(lista):
        return listaNumeros.remove(numeroRemove)
#mostrar
    def mostrarLista(lista):
        return lista
#soma
    def somaLista(lista):
        soma = sum(lista)
        return soma
#media
    def mediaLista(lista):
        media = sum(lista)/len(lista)
        return media
#Opções
    print("1. Adicionar número à lista")
    print("2. Remover um número da lista")
    print("3. Exibir a lista atual")
    print("4. Calcular soma do numeros da lista ")
    print("5. Calcular média dos numeros da lista")
    print("6. Sair")
#laço de repeticao
    while True:
        try:
            entrada = input("Escolha a opção desejada (1/2/3/4/5/6)")
        except Exception:
            print("A opção escolhida não existe!")
        if entrada == "1":
            try:
                numeroAdd = int(input("Qual o número a ser adicionado?"))
                adicionarLista(numeroAdd)
            except ValueError:
                print("O valor digitado não é um número inteiro")
        elif entrada == "2":
            print(listaNumeros)
            numeroRemove = int(input("Qual o número a ser removido?"))
            removerLista(numeroRemove)
        elif entrada == "3":
            print(mostrarLista(listaNumeros))
        elif entrada == "4":
            print(somaLista(listaNumeros))
        elif entrada == "5":
            print(mediaLista(listaNumeros))
        elif entrada == "6":
            break
    print(listaNumeros)
main()