import duckdb

import os
print(os.path.abspath('../data/database.duckdb'))

conn = duckdb.connect('./data/database.duckdb')

result = conn.execute("""
    SELECT * FROM raw.eletronic_sales LIMIT 10;
""").fetchdf()

print(result)

conn.close()
