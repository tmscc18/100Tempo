from io_terminal import imprime_lista

# nome_ficheiro_lista_de_trotinetas = "lista_de_aluguer.pk" # Criar novo ficheiro lista_de_aluguer.pk


def cria_aluguer():
    """ Pede ao utilizador para introduzir uma nova trotineta

    :return: dicionario com uma trotineta na forma 
        {"marca": <<marca>>, "modelo": <<modelo>>, ... COMPLETAR ...}
    """

    nif_cliente = input("NIF do Cliente? ")
    num_serie_troti = input("Série da Trotinete? ")
    hora_data = input("Data e Hora de aluguer? ") # tentar obter automaticamente, do sistema
    return {"nif": nif_cliente, "serie_trotinete": num_serie_troti, "data_hora": hora_data}


def imprime_lista_de_aluguer(lista_de_aluguer):
    """ ..."""

    imprime_lista(cabecalho="Lista de Alugueres", lista=lista_de_aluguer)

