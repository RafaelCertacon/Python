import warnings

from Functions import *

warnings.filterwarnings("ignore")
if __name__ == '__main__':
    div_csv(parts=2, filename="Arquivo_Teste.csv")
    print("Contagem de arquivos")
    print()
    Contagem_arquivo()
    print("Lista dos arquivos")
    print()
    List_arquivos()
    print("Contagem das pastas")
    print()
    Contagem_pastas()
    print("Soma dos pastas")
    print()
    Somar_numero_linhas()
    print("Subtração de linhas")
    print()
    Subtracao_das_linhas()
    Arquivo()
    print(Arquivo())
