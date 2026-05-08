# %%
import pandas as pd

pd.set_option('display.max_columns', None)

# %%

df = pd.read_csv("../data/raw/dataset.csv")

# %%

df.head()

# %%
df.tail()

# %%
df.shape

# %%
df.sample(10)

# %%

# %%
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')
print("Tipos após transformação:")
df.dtypes

# %%
df.head()

# Transformar:
#     - first_purchase_date: string -> datetime YYYY-MM-DD
#     - last_purchase_date: string -> datetime YYYY-MM-DD
#     - order_date: string -> datetime YYYY-MM-DD

# %%
df.info()
# %%
df.duplicated().sum()
# %%
df.isna().sum()
# %%
df['sub_category'].unique()
# %%
df2 = pd.read_parquet("../data/silver/dataset_silver.parquet")
# %%
df2.dtypes
# %%
