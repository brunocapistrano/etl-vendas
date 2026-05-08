# Desafio 3 - Dados de Venda

Pipeline de extração e transformação de dados de vendas de produtos eletrônicos.

## Como Inicializar

```bash
uv sync
uv run python main.py
```

## Estrutura do Projeto

```
desafio-3-dados-de-venda/
├── main.py                      # Entry point
├── src/
│   ├── extract.py               # Download de dados do Google Drive
│   ├── transform.py             # Orquestra a transformação e salva em parquet
│   └── transformations/
│       └── clean.py             # Limpeza: conversão de datas para datetime
├── notebooks/
│   └── nb.py                    # Análise exploratória dos dados
├── data/
│   ├── raw/                     # Dados brutos baixados (CSV)
│   └── silver/                  # Dados transformados (Parquet)
├── pyproject.toml               # Dependências
└── README.md
```

## Fluxo

1. `main.py` chama `extract()` - baixa CSV do Google Drive para `data/raw/dataset.csv`
2. `main.py` chama `transform()` - limpa e salva em `data/silver/dataset_silver.parquet`

## Transformações

- `first_purchase_date`, `last_purchase_date`, `order_date`: convertidos para datetime (YYYY-MM-DD)

## Formato dos Dados

- **Raw**: CSV (lido como string)
- **Silver**: Parquet (preserva tipos, incluindo datetime)

## Dependências

- **gdown**: Download de arquivos do Google Drive
- **pandas**: Manipulação de dados
- **pyarrow**: Suporte a formato Parquet