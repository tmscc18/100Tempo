from datetime import datetime  # para obter data e hora atual
from io_terminal import imprime_lista

nome_ficheiro_lista_de_aluguer = "lista_de_aluguer.pk"


def cria_aluguer():
    """ Pede ao utilizador para introduzir uma nova trotineta
    :return: dicionario com uma trotineta na forma
        {"marca": <<marca>>, "modelo": <<modelo>>, ... COMPLETAR ...}
    """
    nif_cliente = input("NIF do Cliente? ")
    num_serie_troti = input("Série da Trotinete? ")

    # datetime object containing current date and time
    now = datetime.now()  # hora e data obtida automaticamente
    hora_data = now.strftime("%d/%m/%Y %H:%M:%S")  # hora e data muda para formato mais legivel
    print("Data e Hora de aluguer? -> ", hora_data)
    estado_troti = input("Estado da trotinete? ")
    return {"nif": nif_cliente, "serie_trotinete": num_serie_troti, "data_hora": hora_data, "estado": estado_troti}


def imprime_lista_de_aluguer(lista_de_aluguer):
    """ ..."""
    imprime_lista(cabecalho="Lista de Alugueres", lista=lista_de_aluguer)