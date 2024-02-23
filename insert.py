import sqlalchemy
from sqlalchemy import Column, String, Double
from sqlalchemy.orm import declarative_base, sessionmaker

# SQL Alchemy é a ponto do código para o BANCO
engine = sqlalchemy.create_engine(
    'mssql+pyodbc://rafael.rocha:Certa%402024@192.168.0.26/Teste_CertaBot?driver=ODBC+Driver+17+for+SQL+Server',
    echo=True)
# Função base para código em Tabela
Base = declarative_base()


# tabela do Banco de Dados Criada em código REFERENCIA
class Produto(Base):
    __tablename__ = 'Produto'
    id = Column(String(250), primary_key=True, default=str(uuid.uuid4()), autoincrement=True)
    empresa = Column(String(50))
    Produtos = Column(String(50))
    Preco = Column(Double)
    Tipo = Column(String(50))
    Imposto = Column(Double)


# Criação das tabelas
Base.metadata.create_all(engine)

# Cria a sessão do Banco de Dados
Sessao = sessionmaker(bind=engine)
session = Sessao()


# colocando_insert = Produto(
#     id=str(uuid.uuid4()),
#     empresa='Teste01',
#     Produtos='Tablet',
#     Preco=999.99,
#     Tipo=159.65,
#     Imposto=1.1
#
# )


# Add no Banco de Dados
def Inserir(produto):
    session.add(produto)
    session.commit()

# insert_arquivo = Produto(
#     "INSERT INTO users (id, empresa, Produtos, Preco, Tipo, Imposto) VALUES(id.value, empresa.value, Produto.value, Preco.value, Tipo.value, Imposto.value)",
#     Row.id,
#     Row.empresa, Row.Produtos, Row.Preco, Row.Tipo, Row.Imposto)
#
# session.add(colocando_insert)
#
# session.commit()
