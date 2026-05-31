from etl.read_pdf_sisrun import extrair_linhas_pdf
from etl.parse_treinos import capturar_treinos_corrida
from etl.export_csv import montar_tabela
from etl.export_csv import exportar_csv

pdf_path = "data/raw/treinos1.pdf"

linhas = extrair_linhas_pdf(pdf_path)

treinos = capturar_treinos_corrida(linhas)

df = montar_tabela(treinos)

print("\nPRÉVIA DOS DADOS:\n")

print(df.head())

exportar_csv(df)