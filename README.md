# Desafio 3 - Dados de Venda

Pipeline de extração de dados de vendas de produtos eletrônicos.

## Como Inicializar

```bash
uv sync
uv run python main.py
```

## Estrutura do Projeto

```
desafio-3-dados-de-venda/
├── main.py          # Entry point
├── extract.py       # Download de dados do Google Drive
├── data/raw/        # Dados brutos baixados
├── pyproject.toml   # Dependências (gdown)
└── README.md
```

## Fluxo

1. `main.py` chama `extract()` de `extract.py`
2. `extract.py` baixa o CSV do Google Drive para `data/raw/dataset.csv`

## Dependências

- **gdown**: Download de arquivos do Google Drive
