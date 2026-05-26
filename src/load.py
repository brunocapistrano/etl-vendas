import sys
import duckdb
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.config import DB_PATH, RAW_PATH


logger = logging.getLogger(__name__)

def load():
    logger.info("Loading data into DuckDB...")
    
    conn = duckdb.connect(str(DB_PATH))
    
    conn.execute(f"""
                 CREATE OR REPLACE TABLE raw.eletronic_sales AS
                 SELECT * FROM read_csv_auto('{RAW_PATH / 'dataset.csv'}')
                 """)
    
    conn.close()
    logger.info("Data loaded successfully into DuckDB.")
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load()
    
    conn = duckdb.connect('../data/database.duckdb')
    print(conn.execute("SHOW ALL TABLES").fetchdf())
    conn.close()
    