from io_terminal import imprime_lista

nome_ficheiro_lista_de_utilizadores = "lista_de_utilizadores.pk"

def cria_novo_utilizador():
    """ pede os dados de um novo utilizador

    :return: dicionario com o novo utilizador, {"nome": <<nome>>, "email": <<email>>}
    """

    name = input("Introduza o seu nome: ")
    NIF = input("Introduza o seu contribuinte: ")
    phone = input("Introduza o seu telemóvel: ")
    email = input("Introduza o seu email: ")
    password = input("Introduza a sua password: ")

    # todo
    pass


def imprime_lista_de_utilizadores(lista_de_utilizadores):
    """ ..."""

    imprime_lista(cabecalho="Lista de Utilizadores", lista=lista_de_utilizadores)
