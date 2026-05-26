from src.extract import extract
from src.database import init_db
from src.load import load
from src.transform import transform

import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():

    logger.info("Iniciando o processo de extração dos dados...")
    extract()
    logger.info("Processo de extração concluído com sucesso.")
    init_db()  
    load()
    

if __name__ == "__main__":
    main()
