import os

import dask
import sqlalchemy

dask.config.set({'dataframe.query-planning': True})
import dask.dataframe as dd
import pandas as pd


# SQL Alchemy é a ponto do código para o BANCO


def div_csv(parts, filename):
    df = pd.read_csv(filename, encoding='latin1')
    ddf = dd.from_pandas(df, npartitions=parts)
    ddf.to_csv('teste/arquivo*.csv', index=False)

    ddf.compute()
    print('Quantidade de Linhas divididas:', len(ddf))


def Contagem_arquivo():
    linha0 = pd.read_csv('teste/arquivo0.csv', encoding='latin1')
    linha1 = pd.read_csv('teste/arquivo0.csv', encoding='latin1')
    print(len(linha0))
    print(len(linha1))


data = []


def List_arquivos():
    caminho_da_pasta = "C:\\Users\\rafael.rocha\\PycharmProjects\\Certabot\\teste"
    arquivos = os.listdir(caminho_da_pasta)
    for arquivo in arquivos:
        print(f'{caminho_da_pasta}\\{arquivo}')
        caminho_do_arquivo = f'{caminho_da_pasta}\\{arquivo}'
        df = pd.read_csv(caminho_do_arquivo, encoding='UTF-8')
        print(df)


def Contagem_pastas():
    df = os.listdir('teste/')
    print("Quantas pastas tem: ", df)


def Somar_numero_linhas():
    arquivo0 = pd.read_csv('teste/arquivo0.csv', encoding='UTF-8')
    arquivo1 = pd.read_csv('teste/arquivo1.csv', encoding='UTF-8')
    resultado = len(arquivo0) + len(arquivo1)
    print(resultado)


def Subtracao_das_linhas():
    primario = pd.read_csv("Arquivo_Teste.csv", encoding='latin1')
    arquivo0 = pd.read_csv('teste/arquivo0.csv', encoding='latin1')
    arquivo1 = pd.read_csv('teste/arquivo1.csv', encoding='latin1')

    result = (len(primario) - len(arquivo0)) - len(arquivo1)
    print("Subtração deu: ", result)


engine = sqlalchemy.create_engine(
    'mssql+pyodbc://rafael.rocha:Certa%402024@192.168.0.26/Teste_CertaBot?driver=ODBC+Driver+17+for+SQL+Server',
    echo=True)


# conn = sqlalchemy.create_engine('mysql+mysqlconnector://root:somepassword@localhost:3306/db')


# Write the DataFrame to the databasedf.to_sql(name='table_name', con=conn, if_exists='replace', index=False)
# Close the connectionconn.close()

def Arquivo():
    # Abre o arquivo e faz a leitura
    arquivo = pd.read_csv('Arquivo_Teste.csv', encoding='latin1', sep=";")
    # Modifica a coluna "Id" do arquivo principal
    arquivo_final = arquivo.drop("id", axis=1)
    print(arquivo_final)
    # Leitura valor por valor na planilha excel
    for index in arquivo_final.itertuples():
        arquivo_final.to_sql(name="Produto", con=engine, if_exists='append', index=False)
    print(index)
    return arquivo
