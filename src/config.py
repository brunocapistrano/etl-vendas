from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / 'data' / 'database.duckdb'
RAW_PATH = ROOT / 'data' / 'raw'
