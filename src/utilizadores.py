from io_terminal import imprime_lista

nome_ficheiro_lista_de_utilizadores = "lista_de_utilizadores.pk"

def cria_novo_utilizador():
    """ pede os dados de um novo utilizador

    :return: dicionario com o novo utilizador, {"nome": <<nome>>, "email": <<email>>}
    """

    name = input("Introduza o seu nome: ")
    NIF = int(input("Introduza o seu contribuinte: "))
    phone = int(input("Introduza o seu telemóvel: "))
    email = input("Introduza o seu email: ")
    password = input("Introduza a sua password: ")

    return {"name": marca, "NIF": modelo, "phone": phone, "email": email, "password": password}
    # todo
    pass


def imprime_lista_de_utilizadores(lista_de_utilizadores):
    """ ..."""

    imprime_lista(cabecalho="Lista de Utilizadores", lista=lista_de_utilizadores)
