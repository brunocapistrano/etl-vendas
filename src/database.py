import sys
import logging
from pathlib import Path

import duckdb

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.config import DB_PATH


logger = logging.getLogger(__name__)

def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger.info("Conectando ao banco de dados em: %s", DB_PATH)
    conn = duckdb.connect(str(DB_PATH))
    logger.info("Conexão estabelecida com sucesso.")
    return conn

def init_db():
    logger.info("Iniciando inicialização do banco de dados...")
    conn = get_connection()

    conn.execute("CREATE SCHEMA IF NOT EXISTS raw")
    logger.info("Schema 'raw' criado/verificado com sucesso.")

    conn.execute("CREATE SCHEMA IF NOT EXISTS silver")
    logger.info("Schema 'silver' criado/verificado com sucesso.")

    conn.execute("CREATE SCHEMA IF NOT EXISTS gold")
    logger.info("Schema 'gold' criado/verificado com sucesso.")

    conn.close()
    logger.info("Conexão fechada. Inicialização do banco de dados concluída.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    init_db()