"""
Pruebas unitarias para el esquema y la inicialización de la base de datos SQLite.
"""

import sqlite3
import pytest
from pathlib import Path
from src.database import get_db_connection, init_db

@pytest.fixture
def temp_db(tmp_path: Path):
    """Crea una base de datos temporal para pruebas aisladas."""
    test_db_path = tmp_path / "test_meli.db"
    init_db(test_db_path)
    return test_db_path


def test_tables_created(temp_db: Path):
    """Verifica que las 6 tablas esenciales hayan sido creadas."""
    conn = get_db_connection(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = {row["name"] for row in cursor.fetchall()}
    conn.close()

    expected_tables = {
        "ml_listings",
        "source_products",
        "product_matches",
        "fx_rates",
        "opportunities",
        "orders",
    }
    assert expected_tables.issubset(tables), f"Faltan tablas: {expected_tables - tables}"


def test_insert_and_query_ml_listing(temp_db: Path):
    """Verifica que se puedan insertar y consultar publicaciones de Mercado Libre."""
    conn = get_db_connection(temp_db)
    conn.execute(
        """
        INSERT INTO ml_listings (
            id, title, category_id, price, original_price, currency_id,
            seller_id, seller_nickname, seller_power_status, logistic_type,
            free_shipping, sold_quantity, available_quantity, condition,
            permalink, thumbnail, captured_at
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        );
        """,
        (
            "MCO123456789",
            "Memoria RAM DDR4 16GB 3200MHz",
            "MCO1648",
            189900.0,
            219900.0,
            "COP",
            "98765432",
            "TECH_STORE",
            "platinum",
            "fulfillment",
            1,
            50,
            10,
            "new",
            "https://articulo.mercadolibre.com.co/MCO-123456789",
            "https://http2.mlstatic.com/D_123.jpg",
            "2026-11-27T22:30:00Z",
        ),
    )
    conn.commit()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ml_listings WHERE id = ?", ("MCO123456789",))
    row = cursor.fetchone()
    conn.close()

    assert row is not None
    assert row["id"] == "MCO123456789"
    assert row["price"] == 189900.0
    assert row["free_shipping"] == 1
    assert row["logistic_type"] == "fulfillment"


def test_foreign_key_constraint(temp_db: Path):
    """Verifica que la restricción de claves foráneas esté activa."""
    conn = get_db_connection(temp_db)
    with pytest.raises(sqlite3.IntegrityError):
        # Intentar insertar una oportunidad sin un product_match existente
        conn.execute(
            """
            INSERT INTO opportunities (
                match_id, ml_target_price_cop, source_price_usd, trm_used,
                landed_cost_cop, meli_fee_cop, shipping_cost_cop, other_costs_cop,
                net_profit_cop, net_margin, break_even_trm, created_at
            ) VALUES (
                9999, 200000.0, 30.0, 3300.0, 110000.0, 26000.0, 0.0, 3000.0,
                61000.0, 0.305, 4500.0, '2026-11-27T22:30:00Z'
            );
            """
        )
    conn.close()
