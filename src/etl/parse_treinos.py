import re


def capturar_treinos_corrida(linhas):

    treinos = []

    semana_atual = None
    data_atual = None
    treino_atual = None

    for linha in linhas:

        linha = linha.strip()

        # semana
        if "Semana:" in linha:
            semana_atual = linha
            continue

        # data
        if re.fullmatch(r"\d{2}/\d{2}", linha):
            data_atual = linha
            continue

        # início treino corrida
        if "Corrida Rua" in linha:

            if treino_atual:
                treinos.append(treino_atual)

            treino_atual = {
                "semana": semana_atual,
                "data": data_atual,
                "titulo": linha,
                "detalhes": []
            }

            continue

        # capturar detalhes
        if treino_atual:
            treino_atual["detalhes"].append(linha)

    if treino_atual:
        treinos.append(treino_atual)

    return treinos