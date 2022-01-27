import pickle

def le_de_ficheiro(nome_ficheiro):
    """
    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :return: o que leu do ficheiro (depende dos dados guardados)
    """
    try:
        with open(nome_ficheiro, "rb") as f:
            return pickle.load(f)
    except EOFError:
        print("Ficheiros vazios. Ainda não foram introduzidos todos os dados necessarios")
        pass

def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """
    Obtem a lista guardada no ficheiro e imprime essa lista

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """
    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)