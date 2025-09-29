# Importando bibliotecas
import numpy as np
import pandas as pd

# Importando o df
df = pd.read_csv("dados_clean.csv")

# Garantindo que a coluna Data está no formato datetime
df['Data'] = pd.to_datetime(df['Data'])

# Calculando valor total da venda
df["Valor_Total"] = df["Quantidade"] * df["Preco"]

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

# Análise de Vendas por Categoria ao Longo do Ano
vendas_categoria_mensal = df.pivot_table(index=df['Data'].dt.to_period('M'), 
                                         columns='Categoria', 
                                         values='Valor_Total', 
                                         aggfunc='sum').fillna(0)
print("\nVendas Mensais por Categoria:\n", vendas_categoria_mensal)

# Percebe-se que as categorias Papelaria e Eletrônicos são as que mais vendem.
# Em Abril, há um pico em Eletrônicos, possivelmente por conta da Páscoa e promoções relacionadas, mas o destaque mesmo é da Papelaria.
# Papelaria tem seu pico em Junho, o que pode estar relacionado com preparativos para o segundo semestre letivo.
# Em Agosto, há um aumento em Calçados e Vestuários, possivelmente devido ao início do outono e promoções de volta às aulas.
