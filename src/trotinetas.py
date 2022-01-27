from io_terminal import imprime_lista

nome_ficheiro_lista_de_trotinetas = "lista_de_trotinetas.pk"

def cria_trotineta():
    """
    Pede ao utilizador para introduzir uma nova trotineta
    :return: dicionario com uma trotineta na forma, \
    {"marca": marca, \
    "matricula": modelo}
    """
    while True:
        try:
            marca = str(input("marca? "))
            modelo = input("modelo? ").upper()
            print("Bateria: 10 KM ´single charge´")

            return {"marca": marca, "matricula": modelo}

        except (TypeError, ValueError):
            print("\nValor inserido inálido. Use apenas letras para a Marca\n")
            continue


def imprime_lista_de_trotinetas(lista_de_veiculos):
    """
    Obtem a lista guardada no ficheiro e imprime essa lista
    
    :return:
    :param lista_de_veiculos:
    """
    try:
        imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
    except TypeError:
        print("Ficheiro vazio")
        pass