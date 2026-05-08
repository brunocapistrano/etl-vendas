import logging
import os

from src.transformations.clean import clean_data

import pandas as pd


logger = logging.getLogger(__name__)

def path_silver():
    """ Verifica se a pasta 'silver' existe dentro da pasta 'data', caso contrário, cria a pasta. 
        Retorna o caminho completo do arquivo 'dataset_silver.csv' dentro da pasta 'data/silver'. """

    logger.info("Iniciando detecção de output path.")
        
    if not os.path.exists('data'):
        logger.error("Pasta 'data' não existe.")    
    if not os.path.exists('data/silver'):
        os.makedirs('data/silver')
        logger.info("Pasta 'silver' criada com sucesso dentro da pasta 'data'.")

    logger.info("Output path detectado com sucesso.")
    return 'data/silver/'


def transform():
    """ Lê o arquivo 'dataset.csv' da pasta 'data/raw', realiza a transformação dos dados e salva o arquivo transformado na pasta 'data/processed' com o nome 'dataset_transformed.csv'. """

    logger.info("Iniciando a transformação dos dados...")

    df = pd.read_csv('data/raw/dataset.csv')
    
    df_cleaned = clean_data(df)
    
    df_cleaned.to_parquet(f'{path_silver()}dataset_silver.parquet', index=False)