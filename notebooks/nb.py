# %%
import pandas as pd

pd.set_option('display.max_columns', None)

# %%
df = pd.read_csv("../data/raw/dataset.csv")

# %%
df.head()

#%%
df['customer_id'].value_counts()[df['customer_id'].value_counts() > 1]

#%%
df[df['customer_id'] == 'C1380']

# %%
df.tail()

# %%
df.shape

# %%
df.info()

# %%
df.isna().sum()

# %%
df.duplicated().sum()

# %%
df['sub_category'].unique()

# %%
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')
df['first_purchase_date'] = pd.to_datetime(df['first_purchase_date'], format='%Y-%m-%d')
df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'], format='%Y-%m-%d')

df.dtypes

# %%
print("""
CONCLUSÃO:
- Transformar datas (order_date, first_purchase_date, last_purchase_date) para datetime
- Dividir tabela em dimensões: DIM_Geográfica, DIM_Produtos, DIM_Pessoas
""")

# %%
