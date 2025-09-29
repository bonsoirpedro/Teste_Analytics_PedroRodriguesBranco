# Análise de Vendas - Relatório Anual 2023

## 1. Visão Geral do Projeto
Este projeto realiza uma análise exploratória de um conjunto de dados de vendas fictícias de 2023.  
O objetivo principal é extrair **insights valiosos** sobre o desempenho das vendas, identificar **tendências**, produtos mais vendidos e o comportamento do consumidor ao longo do ano.

---

## 2. Estrutura do Projeto
O projeto está organizado da seguinte forma:

```text
├── dados/
│   └── dados_clean.csv         # Dados limpos
│
├── src/
│   ├── limpeza_analise.py            # Criação, limpeza e análise dos dados
│   ├── eda_graficos.py               # Análise exploratória e gráficos
│   ├── create_db.py                  # Criação do banco DuckDB
│   └── consultas_sql.sql             # Queries SQL utilizadas
│
├── img/
│   └── tendencia_vendas_mensais.png  # Gráficos de tendências
│
├── relatorio_insights.md             # Relatório final
└── README.md                         # Documentação do projeto

```
---

## 3. Metodologia
1. **Geração e Limpeza de Dados**  
   - Script: `limpeza_analise.py`  
   - Cria o dataset fictício, remove duplicatas, padroniza nomes de colunas e tipos.  
   - Dados limpos salvos em `dados_clean.csv`.

2. **Análise Exploratória (EDA)**  
   - Script: `eda_graficos.py`  
   - Bibliotecas: Pandas, Matplotlib, Seaborn  
   - Gera métricas principais e gráficos, como `tendencia_vendas_mensais.png`.

3. **Análise SQL**  
   - Script: `create_db.py`  
   - Cria banco de dados DuckDB e registra a tabela `vendas`.  
   - Queries armazenadas em `consultas_sql.sql` para identificar top produtos e análise por períodos.

4. **Relatório Final**  
   - Compilado em `relatorio_insights.md` com as principais descobertas e recomendações.

---

## 4. Principais Insights
- **Categoria com maior faturamento:** Papelaria  
- **Meses de pico de vendas:** Maio e Junho  
- **Produto mais vendido:** Livros  
- **Observações adicionais:**  
  - Eletrônicos e Vestuário apresentaram vendas consistentes, mas com menor faturamento total.  
  - Calçados tiveram maior volatilidade mensal, sugerindo atenção para estoque.  


---

## 5. Tecnologias Utilizadas
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- DuckDB
- SQL  

---

## 6. Próximos Passos (Opcional)
- Criar dashboards interativos (ex.: Streamlit ou Power BI)  
- Analisar top produtos por categoria  
- Avaliar impacto de datas sazonais e promoções  
