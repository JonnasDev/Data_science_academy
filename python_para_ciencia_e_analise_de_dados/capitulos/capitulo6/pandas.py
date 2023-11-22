import pandas as pd

arquivo = 'salarios.csv'

df = pd.read_csv(arquivo)

df.head()

print(df)