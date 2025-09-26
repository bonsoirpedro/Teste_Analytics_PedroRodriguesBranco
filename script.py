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

n = 50

# Agora precisamos gerar os dados fictícios

dados = {
    "ID": np.arange(1, n + 1),
    "Data": pd.to_datetime((np.random.choice(
        pd.date_range("2023-01-01", "2023-12-31"), n)),
    ),
    "Produto": [faker.catch_phrase() for _ in range(n)],
    "Categoria": [faker.word() for _ in range(n)],
    "Quantidade": np.random.randint(1, 100, n),
    "Preço": np.round(np.random.uniform(10.0, 500.0, n), 2),
    "Cidade": [faker.city() for _ in range(n)]
}

df = pd.DataFrame(dados)

print(df.head(10))