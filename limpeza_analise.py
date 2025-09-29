# Importando as bibliotecas necessárias
from faker import Faker
import numpy as np
import pandas as pd
import random

# Vamos fixar as seeds para garantir a reprodutibilidade
seed_valor = 42
faker = Faker('pt_BR')
faker.seed_instance(seed_valor)
np.random.seed(seed_valor)
random.seed(seed_valor)

# Número de registros a serem gerados para o df
n = 200

# Agora precisamos gerar os dados fictícios com a bib Faker e numpy
produtos = ["Notebook", "Smartphone", "Camiseta", "Calça", "Tênis", "Sandália", "Livro", "Caneta"]
categorias = ["Eletrônicos", "Vestuário", "Calçados", "Papelaria"]

dados = {
    "ID": np.arange(1, n + 1),
    "Data": pd.to_datetime((np.random.choice(
        pd.date_range("2023-01-01", "2023-12-31"), n)), # Gera as datas aleatoriamente no intervalo requisitado
    ),
    "Produto": np.random.choice(produtos, n),
    "Categoria": np.random.choice(categorias, n),
    "Quantidade": np.random.randint(1, 100, n),
    "Preço": np.round(np.random.uniform(10.0, 500.0, n), 2),
    "Cidade": [faker.city() for _ in range(n)]
}

df = pd.DataFrame(dados)

print(df.head(10))

# Agora iremos começar o processo de limpeza dos dados

# Verificando se há NAs
df.isna().sum()

# Removendo duplicatas
df = df.drop_duplicates()

# Conversão de tipos de dados, a coluna "Data" deve ser do tipo datetime (mas já está tipada) e as colunas "Produto", "Categoria" e "Cidade" devem ser do tipo categórico
df["Produto"] = df["Produto"].astype("category")
df["Categoria"] = df["Categoria"].astype("category")
df["Cidade"] = df["Cidade"].astype("category")

# Salvar o DataFrame limpo em um arquivo CSV
df.to_csv("dados_clean.csv", index=False)

# Calculando valor total da venda
df["Valor_Total"] = df["Quantidade"] * df["Preço"]

# Print do produto com maior número de vendas totais
produto_mais_vendido = df.groupby("Produto")["Valor_Total"].sum().idxmax()
print(f"Produto com maior número de vendas totais: {produto_mais_vendido}")