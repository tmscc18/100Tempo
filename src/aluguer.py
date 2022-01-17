# todo

from io_terminal import imprime_lista

nome_ficheiro_lista_de_trotinetas = "lista_de_trotinetas.pk"


def cria_trotineta():
    """ Pede ao utilizador para introduzir uma nova trotineta

    :return: dicionario com uma trotineta na forma
        {"marca": <<marca>>, "modelo": <<modelo>>, ... COMPLETAR ...}
    """

    marca = input("marca? ")
    modelo = input("modelo? ").upper()
    return {"marca": marca, "matricula": modelo}


def imprime_lista_de_trotinetas(lista_de_veiculos):
    """ ..."""

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
