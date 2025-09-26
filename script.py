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

# Analise Exploratória de Dados de Venda (EDA)
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Agregação mensal
vendas_mensais = df.resample('M', on='Data')['Valor_Total'].sum()

plt.figure(figsize=(12, 6))
sns.lineplot(x=vendas_mensais.index, y=vendas_mensais.values, 
             marker='o', color='royalblue', linewidth=2)

# Títulos e labels
plt.title('Tendência de Vendas Mensais em 2023', fontsize=14, weight='bold')
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Valor Total de Vendas (R$)', fontsize=12)

# Eixo X com todos os meses
plt.xticks(vendas_mensais.index, vendas_mensais.index.strftime('%b'), rotation=45)

# Formatação do eixo Y como moeda
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'R${x:,.0f}'.replace(',', '.')))

# Linha da média anual
media = vendas_mensais.mean()
plt.axhline(media, color='red', linestyle='--', linewidth=1)
plt.text(vendas_mensais.index[-1], media, f' Média: R${media:,.0f}'.replace(',', '.'), 
         color='red', va='bottom', ha='right', fontsize=10)

# Anotar máximo e mínimo
max_mes = vendas_mensais.idxmax()
min_mes = vendas_mensais.idxmin()
plt.text(max_mes, vendas_mensais.max(), f'⬆ {vendas_mensais.max():,.0f}', 
         ha='center', va='bottom', fontsize=9, color='green')
plt.text(min_mes, vendas_mensais.min(), f'⬇ {vendas_mensais.min():,.0f}', 
         ha='center', va='top', fontsize=9, color='red')

plt.grid(alpha=0.3)
plt.show()

# Análise por Categoria
vendas_categoria = df.groupby('Categoria')['Valor_Total'].sum().sort_values(ascending=False)
print("\nVendas por Categoria:", vendas_categoria)
