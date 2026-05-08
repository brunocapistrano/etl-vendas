from src.extract import extract
from src.transform import transform

import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():

    logger.info("Iniciando o processo de extração dos dados...")
    extract()
    logger.info("Processo de extração concluído com sucesso.")
    
    logger.info("Iniciando o processo de transformação dos dados...")
    transform()
    logger.info("Processo de transformação concluído com sucesso.")

if __name__ == "__main__":
    main()
