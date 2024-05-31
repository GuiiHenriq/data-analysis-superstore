from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# Carregar o dataset
file_path = 'data/raw/superstore_sales.csv'
df = pd.read_csv(file_path, encoding='latin1')

# Conectar ao SQLite
engine = create_engine('sqlite:///data/db/sales_data.db')
conn = engine.connect()

# Importar o dataframe para o SQLite
df.to_sql('superstore', conn, if_exists='replace', index=False)

# Fechar a conexão
conn.close()

df = pd.read_sql('SELECT "Customer Name" FROM superstore WHERE City == "Seattle"', engine)
print(df.head())
print(df.info())