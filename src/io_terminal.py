from tabulate import tabulate


def imprime_lista(cabecalho, lista):
    """ Imprime a :attr:`lista` na forma de uma tabela com um cabeçalho

    Recebe uma lista na forma [{"atrib1": valor 1, "atrib2": valor 2, ...},
    {"atrib1": valor 1, "atrib2": valor 2, ...}, ...] e imprime no terminal uma tabela
    na forma

    ==  ======  ======
    id  atrib1  atrib2
    ==  ======  ======
    0   valor1  valor2
    1   ...      ...
    ==  ======  ======

    :param cabecalho: cabecalho para a listagem
    :param lista: lista a ser impressa
    """

    cabecalho = f":::::::::::::::::: {cabecalho} ::::::::::::::::::"
    comprimento_cabecalho = len(cabecalho)

    print(cabecalho)
    imprime_lista_de_dicionarios(lista)
    print(comprimento_cabecalho * ":")


def imprime_lista_de_dicionarios(lista):
    """
    .... todo ....
    :param lista:
    :return:
    """
    if len(lista) > 0:
        # cabecalho da tabela
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        # dados
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

        print(tabulate(lista_a_imprimir, headers="firstrow"))
    else:
        print("lista vazia")
