import logging

from src.config import ROOT, RAW_PATH
from src.transformations.clean import type_transform

import pandas as pd


logger = logging.getLogger(__name__)

def path_silver():
    silver_path = ROOT / 'data' / 'silver'
    silver_path.mkdir(parents=True, exist_ok=True)
    logger.info("Pasta 'silver' criada/verificada com sucesso em: %s", silver_path)
    return silver_path


def transform():
    logger.info("Iniciando a transformação dos dados...")

    df = pd.read_csv(str(RAW_PATH / 'dataset.csv'))
    
    df_cleaned = type_transform(df)
    
    df_cleaned.to_parquet(str(path_silver() / 'dataset_silver.parquet'), index=False)