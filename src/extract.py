import os
import logging

import gdown


logger = logging.getLogger(__name__)

def path():
    """ Verifica se a pasta 'data' existe, caso contrário, cria a pasta. 
        Verifica se a pasta 'raw' existe dentro da pasta 'data', caso contrário, cria a pasta.
        Retorna o caminho completo do arquivo 'dataset.csv' dentro da pasta 'data'. """

    logger.info("Iniciando detecção de output path.")
        
    if not os.path.exists('data'):
        os.makedirs('data')
        logger.info("Pasta 'data' criada com sucesso.")    
    if not os.path.exists('data/raw'):
        os.makedirs('data/raw')
        logger.info("Pasta 'raw' criada com sucesso dentro da pasta 'data'.")

    logger.info("Output path detectado com sucesso.")
    return 'data/raw/dataset.csv'

def extract():
    
    logger.info("Iniciando a extração dos dados...")
    
    url = 'https://drive.google.com/file/d/1d5wTklqhJxyuVQdtfJkAqPC8BFzM-JI0/view?usp=sharing'
    gdown.download(url=url, output=path())
    
if __name__ == "__main__":    
    extract()