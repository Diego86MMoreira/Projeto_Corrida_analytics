import pdfplumber

def extrair_linhas_pdf(pdf_path):

    linhas = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            texto = page.extract_text()

            if texto:
                linhas.extend(texto.split("\n"))

    return linhas