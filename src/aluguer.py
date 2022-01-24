from datetime import datetime  # para obter data e hora atual
from io_terminal import imprime_lista

nome_ficheiro_lista_de_aluguer = "lista_de_aluguer.pk"


def cria_aluguer():
    """ Pede ao utilizador para introduzir uma nova trotineta
    :return: dicionario com uma trotineta na forma
        {"marca": <<marca>>, "modelo": <<modelo>>, ... COMPLETAR ...}
    """
    while True:
        try:
            nif_cliente = int(input("NIF do Cliente? "))
            num_serie_troti = int(input("Modelo da Trotinete? "))

            # datetime object containing current date and time
            now = datetime.now()  # hora e data obtida automaticamente
            hora_data = now.strftime("%d/%m/%Y %H:%M:%S")  # hora e data muda para formato mais legivel
            print("Data e Hora de aluguer? -> ", hora_data)

            estado_troti = int(input("Estado da trotinete(0 a 10)? "))
            if estado_troti >= 0 and estado_troti <= 10:
                pass
            else:
                print("Valor insirido em \"Estado da Trotinete\" é invalido\n")
                continue

            return {"nif": nif_cliente, "serie_trotinete": num_serie_troti, "data_hora": hora_data, "estado": estado_troti}

        except (TypeError, ValueError):
            print("Valor inserido inálido. Use apenas digidos\n")
            continue

def imprime_lista_de_aluguer(lista_de_aluguer):
    """ ..."""
    try:
        imprime_lista(cabecalho="Lista de Alugueres", lista=lista_de_aluguer)
    except TypeError:
        print("Ficheiro vazio")
        pass

