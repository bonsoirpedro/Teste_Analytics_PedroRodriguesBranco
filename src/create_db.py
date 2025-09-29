# Importando a biblioteca duckdb e pandas
import pandas as pd
import duckdb

# Importando o DataFrame limpo
df = pd.read_csv("dados_clean.csv")
df['Data'] = pd.to_datetime(df['Data']) # Garantindo que a coluna Data está no formato datetime

# Criando um banco de dados DuckDB na memória
con = duckdb.connect(database=':memory:')
con.execute("CREATE TABLE vendas AS SELECT * FROM df")
print("Banco de dados DuckDB criado com sucesso na memória.")

# Listando as tabelas no banco de dados
tables = con.execute("SHOW TABLES").fetchall()
print("Tabelas no banco de dados DuckDB:", tables)

# Listando o nome do produto, categoria e soma total de vendas (Quantidade * Preço) para cada produto e ordenado em decrescente pelo valor total de vendas
query = """
SELECT Produto, Categoria, SUM(Quantidade * Preco) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;
"""
res = con.execute(query).fetchdf()

print(res.head(10))  # Mostrando as 10 primeiras linhas do resultado

# Iddentificando os produtos que venderam menos em junho de 2023.
query_junho = """
SELECT Produto, Categoria, SUM(Quantidade * Preco) AS Total_Vendas_Junho
FROM vendas
WHERE strftime(Data, '%Y-%m') = '2023-06'
GROUP BY Produto, Categoria
ORDER BY Total_Vendas_Junho ASC;
"""
res_junho = con.execute(query_junho).fetchdf()
print(res_junho.head())

# Salvando as consultas em um arquivo SQL
with open("consultas_sql.sql", "w") as file:
    file.write(query + "\n\n" + query_junho)
print("Consultas SQL salvas em 'consultas_sql.sql'.")
# Fechando a conexão com o banco de dados
con.close()