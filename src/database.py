"""
Módulo de inicialización y gestión de la base de datos SQLite (data/meli.db).
Crea y gestiona las 6 tablas esenciales del proyecto:
- ml_listings
- source_products
- product_matches
- fx_rates
- opportunities
- orders
"""

import sqlite3
from pathlib import Path
from typing import Optional

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "meli.db"

SCHEMA_SQL = """
-- 1. Publicaciones capturadas de Mercado Libre
CREATE TABLE IF NOT EXISTS ml_listings (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category_id TEXT,
    price REAL NOT NULL,
    original_price REAL,
    currency_id TEXT DEFAULT 'COP',
    seller_id TEXT,
    seller_nickname TEXT,
    seller_power_status TEXT,
    logistic_type TEXT,
    free_shipping INTEGER DEFAULT 0,
    sold_quantity INTEGER,
    available_quantity INTEGER,
    condition TEXT,
    permalink TEXT,
    thumbnail TEXT,
    captured_at TEXT NOT NULL
);

-- 2. Catálogo de productos vigilados en proveedores externos (Amazon, eBay)
CREATE TABLE IF NOT EXISTS source_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,              -- 'amazon', 'ebay'
    source_id TEXT NOT NULL,           -- ASIN o eBay Item ID
    title TEXT NOT NULL,
    brand TEXT,
    model TEXT,
    part_number TEXT,
    specs_json TEXT,                   -- JSON con specs (capacidad, velocidad, etc.)
    current_price_usd REAL,
    shipping_usd REAL DEFAULT 0.0,
    url TEXT,
    last_checked_at TEXT,
    UNIQUE(source, source_id)
);

-- 3. Equivalencias curadas manualmente entre Mercado Libre y proveedores
CREATE TABLE IF NOT EXISTS product_matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ml_item_id TEXT NOT NULL,
    source_product_id INTEGER NOT NULL,
    curated_by TEXT DEFAULT 'julian',
    curation_status TEXT DEFAULT 'approved', -- 'approved', 'rejected', 'pending'
    notes TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY(ml_item_id) REFERENCES ml_listings(id),
    FOREIGN KEY(source_product_id) REFERENCES source_products(id),
    UNIQUE(ml_item_id, source_product_id)
);

-- 4. Histórico diario de la TRM oficial de Colombia
CREATE TABLE IF NOT EXISTS fx_rates (
    date TEXT PRIMARY KEY,             -- YYYY-MM-DD
    official_rate REAL NOT NULL,       -- TRM certificada Superfinanciera
    effective_rate REAL NOT NULL,      -- TRM oficial * (1 + spread)
    source TEXT DEFAULT 'datos.gov.co',
    created_at TEXT NOT NULL
);

-- 5. Oportunidades detectadas y márgenes proyectados
CREATE TABLE IF NOT EXISTS opportunities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    ml_target_price_cop REAL NOT NULL,
    source_price_usd REAL NOT NULL,
    trm_used REAL NOT NULL,
    landed_cost_cop REAL NOT NULL,
    meli_fee_cop REAL NOT NULL,
    shipping_cost_cop REAL NOT NULL,
    other_costs_cop REAL NOT NULL,
    net_profit_cop REAL NOT NULL,
    net_margin REAL NOT NULL,
    break_even_trm REAL NOT NULL,
    status TEXT DEFAULT 'pending',     -- 'pending', 'approved', 'rejected', 'ordered'
    created_at TEXT NOT NULL,
    FOREIGN KEY(match_id) REFERENCES product_matches(id)
);

-- 6. Registro de compras reales realizadas y sus costos efectivos para calibración
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference_code TEXT,
    product_name TEXT NOT NULL,
    source TEXT NOT NULL,              -- 'amazon', 'ebay'
    source_order_id TEXT,
    purchase_date TEXT NOT NULL,
    purchase_price_usd REAL NOT NULL,
    fx_rate_charged REAL NOT NULL,     -- TRM real cobrada por el banco
    international_shipping_cop REAL DEFAULT 0.0,
    import_taxes_cop REAL DEFAULT 0.0,
    total_landed_cost_cop REAL NOT NULL,
    sale_platform TEXT,                -- 'mercadolibre', 'facebook_marketplace'
    sale_date TEXT,
    sale_price_cop REAL,
    platform_fee_cop REAL DEFAULT 0.0,
    local_shipping_cop REAL DEFAULT 0.0,
    real_net_profit_cop REAL,
    real_net_margin REAL,
    notes TEXT
);

-- Índices de consulta frecuente
CREATE INDEX IF NOT EXISTS idx_ml_listings_category ON ml_listings(category_id);
CREATE INDEX IF NOT EXISTS idx_ml_listings_captured ON ml_listings(captured_at);
CREATE INDEX IF NOT EXISTS idx_opportunities_status ON opportunities(status);
CREATE INDEX IF NOT EXISTS idx_product_matches_status ON product_matches(curation_status);
"""


def get_db_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Retorna una conexión a la base de datos SQLite con soporte para claves foráneas."""
    path = db_path or DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(db_path: Optional[Path] = None) -> None:
    """Ejecuta el script DDL de creación de tablas en la base de datos."""
    conn = get_db_connection(db_path)
    try:
        conn.executescript(SCHEMA_SQL)
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Base de datos SQLite inicializada exitosamente en: {DB_PATH}")
