# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
import random

# Vamos fixar as seeds para garantir a reprodutibilidade
seed_valor = 42
np.random.seed(seed_valor)
random.seed(seed_valor)

# Número de registros a serem gerados para o df
n = 200

# Lista de pares produto-categoria
produtos_categorias = [
    ("Notebook", "Eletrônicos"),
    ("Smartphone", "Eletrônicos"),
    ("Camiseta", "Vestuário"),
    ("Calça", "Vestuário"),
    ("Tênis", "Calçados"),
    ("Sandália", "Calçados"),
    ("Livro", "Papelaria"),
    ("Caneta", "Papelaria")
]

# Agora precisamos sortear os produtos para cada registro
escolhas = np.random.choice(len(produtos_categorias), n)

# gerar os dados
dados = {
    "ID": np.arange(1, n + 1),
    "Data": pd.to_datetime(np.random.choice(
        pd.date_range("2023-01-01", "2023-12-31"), n)),
    "Produto": [produtos_categorias[i][0] for i in escolhas],
    "Categoria": [produtos_categorias[i][1] for i in escolhas],
    "Quantidade": np.random.randint(1, 100, n),
    "Preco": np.round(np.random.uniform(10.0, 500.0, n), 2)
}

df = pd.DataFrame(dados)

print(df.head(10))

# Agora iremos começar o processo de limpeza dos dados

# Verificando se há NAs
df.isna().sum()

# Removendo duplicatas
df = df.drop_duplicates()

# Conversão de tipos de dados, a coluna "Data" deve ser do tipo datetime e as colunas "Produto", "Categoria" e "Cidade" devem ser do tipo categórico
df["Produto"] = df["Produto"].astype("category")
df["Categoria"] = df["Categoria"].astype("category")
df['Data'] = pd.to_datetime(df['Data'])

# Salvar o DataFrame limpo em um arquivo CSV
df.to_csv("dados_clean.csv", index=False)

# Calculando valor total da venda
df["Valor_Total"] = df["Quantidade"] * df["Preco"]

# Print do produto com maior número de vendas totais
produto_mais_vendido = df.groupby("Produto")["Valor_Total"].sum().idxmax()
print(f"Produto com maior número de vendas totais: {produto_mais_vendido}")