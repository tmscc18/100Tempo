import pickle


def le_de_ficheiro(nome_ficheiro):
    """ le os dados de um ficheiro

    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :return: o que leu do ficheiro (depende dos dados guardados)
    """

    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)


def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """ guarda os dados recebidos num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)
