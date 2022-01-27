from io_terminal import imprime_lista

nome_ficheiro_lista_de_report = "lista_de_report.pk"

def cria_report(clientid):
    """
    Pede ao utilizador para introduzir um novo reporte mas tem que haver obrigatoriamente um utilizador antes criado
    :return: dicionario com um reporte na forma, {"clientid": clientid, "tipo": tipo, "story": story}
    """
    while True:
        try:
            print("\nId do Cliente? ->", clientid)
            tipo = str(input("Tipo de report? "))
            story = str(input("Descrição? "))
            return {"clientid": clientid, "tipo": tipo, "story": story}
        except (TypeError, ValueError):
            print("Valor inserido inálido. Use apenas letras\n")
            continue


def imprime_lista_de_report(lista_de_report):
    """
    :Obtem a lista guardada no ficheiro e imprime essa lista
    """
    try:
        imprime_lista(cabecalho="Lista de Reportes", lista=lista_de_report)
    except TypeError:
        print("Ficheiro vazio")
        pass