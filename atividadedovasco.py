import random
listaNumeros = [random.randint(1,100) for _ in range(5)]

#adicionar a lista
def adicionarLista(listaNumeros, numeroAdd):
    """
    Adiciona o número escrito à listaNumeros
    """
    add = int(numeroAdd)
    return listaNumeros.append(add)

#remover da lista
def removerLista(listaNumeros, numeroRemover):
    """
    Remove o número escrito da listaNumeros, caso o número não exista, entrará no except e continuará o loop
    """
    rem = int(numeroRemover)
    return listaNumeros.remove(rem)

#mostrar a lista
def mostrarLista(lista):
    """
    Dá output na lista existente por meio de um print
    """
    return lista

#soma da lista
def somaLista(lista):
    """
    Realiza a soma dos números presentes na lista
    """
    soma = sum(lista)
    return soma

#media da lista
def mediaLista(lista):
    """
    Realiza a média aritmética dos números presentes na lista
    """
    media = sum(lista)/len(lista)
    return media

def main():
    
#Opções de entrada
    print("1. Adicionar número à lista")
    print("2. Remover um número da lista")
    print("3. Exibir a lista atual")
    print("4. Calcular soma do numeros da lista ")
    print("5. Calcular média dos numeros da lista")
    print("6. Sair")

#laço de repeticao
    while True:

        #tentativa do input inicial
        try:
            #input inicial, define qual função sera executada
            entrada = int(input("Escolha a opção desejada (1/2/3/4/5/6) "))

        #qualquer valor de entrada que dê erro
        except Exception:
            print("A opção escolhida não é válida!")
            continue
        
        #caso a entrada não exista nas opções
        if entrada > 8 or entrada <= 0:
            print("A opção escolhida não existe!")

        #entrada escolhida é opção 1 (adicionar número a lista)
        if entrada == 1:

            #tentativa de pedir um número a ser adicionado na lista, 
            #sendo necessario ser um número inteiro
            try:
                numeroAdd = int(input("Qual o número a ser adicionado? "))
                adicionarLista(listaNumeros, numeroAdd)
                print(listaNumeros)

            #excessão caso o que for digitado não seja um número inteiro
            except ValueError:
                print("O valor digitado não é um número inteiro")

        #entrada escolhida é opção 2 (remover número da lista)
        elif entrada == 2:

            #print da lista atual para facilitar remoção de valor
            print(listaNumeros)

            #tentativa de pedir um número a ser removido da lista,
            #sendo necessário ser um número inteiro
            try:
                numeroRemove = int(input("Qual o número a ser removido? "))
                removerLista(listaNumeros, numeroRemove)
                print(listaNumeros)

            #excessão caso o número digitado não estiver na lista, 
            #ou caso o que foi digitado não seja um número
            except ValueError:
                print("O valor digitado não existe na lista, ou não é um número!")

        #entrada escolhida é opção 3 (mostrar a lista)
        elif entrada == 3:
            print(mostrarLista(listaNumeros))
        
        #entrada escolhida é a opção 4 (somar valores da lista)
        elif entrada == 4:
            print(somaLista(listaNumeros))

        #entrada escolhida é a opção 5 (fazer média dos números da lista)
        elif entrada == 5:

            #tentativa de fazer a média dos valores existentes
            try:
                print(mediaLista(listaNumeros))

            #excessão caso não haja valores na lista, já que a divisão de 0 por 0 é impossível
            except Exception:
                print("Não há valores na lista!")

        #entrada escolhida é a opção 6 (terminar o programa)
        elif entrada == 6:
            break

    #print final para apresentar a lista antes do programa acabar
    print(listaNumeros)
if __name__ == '__main__':
    main()