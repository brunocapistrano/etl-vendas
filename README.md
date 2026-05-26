# Desafio 3 - Dados de Venda

Pipeline ETL de dados de vendas de produtos eletrônicos com DuckDB.

## Como Inicializar

```bash
uv sync
uv run python pipeline.py
```

## Estrutura do Projeto

```
desafio-3-dados-de-venda/
├── pipeline.py                   # Entry point do pipeline ETL
├── src/
│   ├── config.py                 # Caminhos absolutos do projeto
│   ├── database.py               # Conexão e inicialização do DuckDB (schemas)
│   ├── extract.py                # Download de dados do Google Drive
│   ├── load.py                   # Carga do CSV para o DuckDB
│   ├── transform.py              # Orquestra a transformação e salva em parquet
│   └── transformations/
│       └── clean.py              # Limpeza: conversão de datas para datetime
├── notebooks/
│   ├── nb.py                     # Análise exploratória dos dados
│   └── query_duck_db.py          # Queries no DuckDB
├── data/
│   ├── raw/                      # Dados brutos baixados (CSV)
│   ├── silver/                   # Dados transformados (Parquet)
│   └── database.duckdb           # Banco DuckDB
├── pyproject.toml                # Dependências
├── uv.lock                       # Lockfile do uv
└── README.md
```

## Fluxo

1. `pipeline.py` chama `extract()` - baixa CSV do Google Drive para `data/raw/dataset.csv`
2. `pipeline.py` chama `init_db()` - cria schemas `raw`, `silver` e `gold` no DuckDB
3. `pipeline.py` chama `load()` - carrega o CSV para a tabela `raw.eletronic_sales`
4. `pipeline.py` chama `transform()` - limpa datas e salva em `data/silver/dataset_silver.parquet`

## Transformações

- `first_purchase_date`, `last_purchase_date`, `order_date`: convertidos para datetime (YYYY-MM-DD)

## Formato dos Dados

- **Raw**: CSV (lido como string)
- **DuckDB**: Banco relacional com schemas `raw`, `silver`, `gold`
- **Silver**: Parquet (preserva tipos, incluindo datetime)

## Dependências

- **duckdb**: Banco de dados SQL embarcado
- **gdown**: Download de arquivos do Google Drive
- **pandas**: Manipulação de dados
- **pyarrow**: Suporte a formato Parquet
