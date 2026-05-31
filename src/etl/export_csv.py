import pandas as pd
import re


def montar_tabela(treinos):

    registros = []

    for treino in treinos:

        titulo = treino["titulo"]

        km = None

        km_match = re.search(r"(\d+(?:\.\d+)?)\s*Km", titulo)

        if km_match:
            km = float(km_match.group(1))

        zona = None

        zona_match = re.search(r"(Z\d)", titulo)

        if zona_match:
            zona = zona_match.group(1)

        fc_min = None
        fc_max = None

        for linha in treino["detalhes"]:

            m1 = re.search(r"FC Min:\s*(\d+)", linha)

            if m1:
                fc_min = int(m1.group(1))

            m2 = re.search(r"FC Máx:\s*(\d+)", linha)

            if m2:
                fc_max = int(m2.group(1))

        registros.append(
            {
                "data": treino["data"],
                "semana": treino["semana"],
                "titulo": titulo,
                "km": km,
                "zona": zona,
                "fc_min": fc_min,
                "fc_max": fc_max,
            }
        )

    return pd.DataFrame(registros)


def exportar_csv(df):

    caminho = "data/processed/treinos_planejados.csv"

    df.to_csv(
        caminho,
        index=False,
        sep=";",
        encoding="utf-8-sig"
    )

    print(f"\nCSV criado: {caminho}")