from io_terminal import imprime_lista

nome_ficheiro_lista_de_utilizadores = "lista_de_utilizadores.pk"

def cria_novo_utilizador():
    """ pede os dados de um novo utilizador

    :return: dicionario com o novo utilizador, {"nome": <<nome>>, "email": <<email>>}
    """
    while True:
        try:
            nome = str(input("\nNome? "))
            email = str(input("Email? "))
            telemovel = int(input("Telemovel? "))
            password = input("Password? ")
            return {"nome": nome, "email": email, "telemovel": telemovel, "password": password}

        except (TypeError, ValueError):
            print("\nValor inserido inálido. Use apenas digidos para o Telemóvel e letras para os outros campos\n")
            continue


def imprime_lista_de_utilizadores(lista_de_utilizadores):
    """ ..."""
    try:
        imprime_lista(cabecalho="Lista de Utilizadores", lista=lista_de_utilizadores)
    except TypeError:
        print("Ficheiro vazio")
        pass
