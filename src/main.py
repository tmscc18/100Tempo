
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
from aluguer import (
    cria_aluguer,
    imprime_lista_de_aluguer,
    nome_ficheiro_lista_de_aluguer
)

from report import (
    cria_report,
    imprime_lista_de_report,
    nome_ficheiro_lista_de_report
)

from io_terminal import (
    imprime_lista_de_dicionarios
)
import time

def menu():

    lista_de_trotinetas = []
    lista_de_utilizadores = []
    lista_de_compras = []
    lista_de_aluguer = []
    lista_de_report = []


    while True:
        """ main menu da aplicação - Direciona aos locais adequados consuante a escolha"""
        print("""
        *********************************************************************
        :                   A trote - aluguer de trotinetas                 :
        *********************************************************************
        :                                                                   :
        : tn - nova trotineta       tl - lista veiculos                     :
        : un - novo utilizador      ul - lista utilizadores                 :
        : an - novo aluguer         al - lista aluguers                     :
        :                                                                   :
        : rp - novo reporte         rl - lista reportes                     :
        : ...                                                               :
        : g - guarda tudo           c - carrega tudo                        :
        :                                                                   :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("opcao? -> ").lower()

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
            guarda_as_listas_em_ficheiros(lista_de_trotinetas, lista_de_utilizadores, lista_de_aluguer, lista_de_report)
        elif op == "c":
            lista_de_trotinetas, lista_de_utilizadores, lista_de_aluguer, lista_de_report = carrega_as_listas_dos_ficheiros()
        elif op == "an":
            if lista_de_utilizadores and lista_de_trotinetas:
                id_comprador = pergunta_id(questao="Qual o id do comprador?", lista=lista_de_utilizadores)
                id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_trotinetas)
                novo_aluguer = cria_aluguer()
                lista_de_aluguer.append(novo_aluguer)
                lista_de_compras.append([id_comprador, id_veiculo, time.time()])
            else:
                print("Erro: tem de ter utilizadores e trotinetas")
        elif op == "al":
            imprime_lista_de_aluguer(lista_de_aluguer)

        elif op == "rp":
            if lista_de_utilizadores:
                id_comprador = pergunta_id(questao="Qual o seu id de cliente?", lista=lista_de_utilizadores, show=0)
                novo_report = cria_report(id_comprador)
                lista_de_report.append(novo_report)
            else:
                print("Erro: tem de ter utilizadores")

        elif op == "rl":
            imprime_lista_de_report(lista_de_report)



def pergunta_id(questao, lista, show=1):
    """
    :param questao: "Qual o seu id de cliente?"
    :param lista: lista_de_utilizadores
    :return: idx (tabela)

    :verificação da existencia de valores pre-existentes noutra lista
    """
    if show == 1:
        imprime_lista_de_dicionarios(lista)
        while True:
            idx = int(input(questao))
            if 0 <= idx < len(lista):
                return idx
            else:
                print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")
    elif show == 0:
        # foi removida a opção de mostrar a lista, para nao mostrar as passwords e infromações de outros clientes
        while True:
            idx = int(input(questao))
            if 0 <= idx < len(lista):
                return idx
            else:
                print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")

def carrega_as_listas_dos_ficheiros():
    """ Carrega as listas dos ficheiros para uma lista que vai guardar num ficheiro adequado"""

    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_trotinetas)
    lista_de_utilizadores = le_de_ficheiro(nome_ficheiro_lista_de_utilizadores)
    lista_de_aluguer = le_de_ficheiro(nome_ficheiro_lista_de_aluguer)
    lista_de_report = le_de_ficheiro(nome_ficheiro_lista_de_report)
    return lista_de_veiculos, lista_de_utilizadores, lista_de_aluguer, lista_de_report


def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_utilizadores, lista_de_aluguer, lista_de_report):
    """
    :param lista_de_utilizadores: lista_de_utilizadores
    :param lista_de_veiculos: lista_de_veiculos
    :return: Guarda as listas nos ficheiros apropriados
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (S/n)? ")
    if op in ['s', 'S', '']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_trotinetas, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_utilizadores, lista_de_utilizadores)
        guarda_em_ficheiro(nome_ficheiro_lista_de_aluguer, lista_de_aluguer)
        guarda_em_ficheiro(nome_ficheiro_lista_de_report, lista_de_report)
    else:
        print("Cancelada.")


if __name__ == "__main__":
    menu()
