from io_terminal import imprime_lista

nome_ficheiro_lista_de_utilizadores = "lista_de_utilizadores.pk"

def cria_novo_utilizador():
    """ pede os dados de um novo utilizador

    :return: dicionario com o novo utilizador, {"nome": <<nome>>, "email": <<email>>}
    """
    nome = input("NIF do Cliente? ")
    email = input("Série da Trotinete? ")


    print("Data e Hora de aluguer? -> ", hora_data)
    estado_troti = input("Estado da trotinete? ")
    return {"nif": nif_cliente, "serie_trotinete": num_serie_troti, "data_hora": hora_data, "estado": estado_troti}


def imprime_lista_de_utilizadores(lista_de_utilizadores):
    """ ..."""

    imprime_lista(cabecalho="Lista de Utilizadores", lista=lista_de_utilizadores)
