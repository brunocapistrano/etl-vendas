from extract import extract

import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():

    logger.info("Iniciando o processo de extração dos dados...")
    extract()

if __name__ == "__main__":
    main()
