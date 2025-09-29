
SELECT Produto, Categoria, SUM(Quantidade * Preco) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;



SELECT Produto, Categoria, SUM(Quantidade * Preco) AS Total_Vendas_Junho
FROM vendas
WHERE strftime(Data, '%Y-%m') = '2023-06'
GROUP BY Produto, Categoria
ORDER BY Total_Vendas_Junho ASC;
