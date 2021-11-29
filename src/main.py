# tiago CAstro

from trotinetas import (
    cria_trotineta,
    imprime_lista_de_trotinetas,
    nome_ficheiro_lista_de_trotinetas
)
from utilizadores import (
    cria_novo_utilizador,
    imprime_lista_de_utilizadores,
    nome_ficheiro_lista_de_utilizadores
)
from io_ficheiros import (
    guarda_em_ficheiro,
    le_de_ficheiro
)
from io_terminal import (
    imprime_lista_de_dicionarios
)
import time


def menu():
    """ main menu da aplicação"""

    lista_de_trotinetas = []
    lista_de_utilizadores = []
    lista_de_compras = []
# boas
    while True:
        print("""
        *********************************************************************
        :       A trote - aluguer de trotinetas                             : 
        *********************************************************************
        :                                                                   :
        : tn - nova trotineta       tl - lista veiculos                     :
        : un - novo utilizador      ul - lista utilizadores                 :
        : an - novo aluguer         al - lista aluguers                     :
        : ...                                                               :
        : ...                                                               :
        : ...                                                               :
        : g - guarda tudo           c - carrega tudo                        :
        :                                                                   :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("opcao?").lower()

        if op == "x":
            exit()
        elif op == "tn":
            nova_trotineta = cria_trotineta()
            lista_de_trotinetas.append(nova_trotineta)
        elif op == "tl":
            imprime_lista_de_trotinetas(lista_de_trotinetas)
        elif op == "un":
            novo_utilizador = cria_novo_utilizador()
            lista_de_utilizadores.append(novo_utilizador)
        elif op == "ul":
            imprime_lista_de_utilizadores(lista_de_utilizadores)
        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_trotinetas, lista_de_utilizadores)
        elif op == "c":
            lista_de_trotinetas, lista_de_utilizadores = carrega_as_listas_dos_ficheiros()
        elif op == "an":
            if lista_de_utilizadores and lista_de_trotinetas:
                id_comprador = pergunta_id(questao="Qual o id do comprador?", lista=lista_de_utilizadores)
                id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_trotinetas)
                lista_de_compras.append([id_comprador, id_veiculo, time.time()])
            else:
                print("Erro: tem de ter utilizadores e trotinetas")
        elif op == "al":
            pass
            # todo
            # imprime_lista_de_compras()


def pergunta_id(questao, lista):
    """ ... ??to do??

    :param questao:
    :param lista:
    :return:
    """

    imprime_lista_de_dicionarios(lista)
    while True:
        idx = int(input(questao))
        if 0 <= idx < len(lista):
            return idx
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")


def carrega_as_listas_dos_ficheiros():
    """ ...todo... """

    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_trotinetas)
    lista_de_utilizadores = le_de_ficheiro(nome_ficheiro_lista_de_utilizadores)
    return lista_de_veiculos, lista_de_utilizadores


def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_utilizadores):
    """ ... todo ....

    :param lista_de_utilizadores:
    :param lista_de_veiculos:
    :return:
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (S/n)?")
    if op in ['s', 'S', '']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_trotinetas, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_utilizadores, lista_de_utilizadores)
    else:
        print("Cancelada.")


if __name__ == "__main__":
    menu()
