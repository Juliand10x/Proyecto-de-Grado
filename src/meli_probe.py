"""
Script de auditoría y exploración empírica de la API de Mercado Libre Colombia (MCO).
Prueba endpoint por endpoint sin token para verificar qué datos entrega realmente
y guarda las respuestas crudas en data/raw/ con marca de tiempo ISO.
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional
import requests

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

BASE_URL = "https://api.mercadolibre.com"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def save_raw_response(endpoint_name: str, data: Any) -> Path:
    """Guarda la respuesta cruda intacta en data/raw/ con timestamp ISO."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    filename = f"meli_raw_{endpoint_name}_{timestamp}.json"
    filepath = RAW_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logging.info(f"Dato crudo guardado en: {filepath.name}")
    return filepath


def probe_endpoint(name: str, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Ejecuta una petición GET y analiza el status code, headers y payload."""
    logging.info(f"Probando endpoint [{name}]: {url}")
    try:
        response = requests.get(url, params=params, timeout=12)
        status_code = response.status_code
        try:
            body = response.json()
        except Exception:
            body = {"raw_text": response.text[:500]}

        saved_file = save_raw_response(name, {
            "probe_name": name,
            "url": url,
            "params": params,
            "status_code": status_code,
            "headers": dict(response.headers),
            "body": body
        })

        return {
            "name": name,
            "url": url,
            "status_code": status_code,
            "works_without_token": status_code == 200,
            "file": saved_file.name,
            "body": body
        }
    except Exception as e:
        logging.error(f"Error al probar {name}: {e}")
        return {
            "name": name,
            "url": url,
            "status_code": 0,
            "works_without_token": False,
            "error": str(e)
        }


def run_full_probe() -> Dict[str, Any]:
    """Ejecuta la batería de pruebas sobre los endpoints clave de Mercado Libre Colombia."""
    results = {}

    # 1. Búsqueda por término (Memorias RAM)
    results["search_keyword"] = probe_endpoint(
        "search_ram",
        f"{BASE_URL}/sites/MCO/search",
        params={"q": "memoria ram ddr4 16gb", "limit": 5}
    )

    # 2. Categorías del sitio MCO
    results["site_categories"] = probe_endpoint(
        "site_categories",
        f"{BASE_URL}/sites/MCO/categories"
    )

    # 3. Detalle de categoría Computación (MCO1648)
    results["category_detail"] = probe_endpoint(
        "category_computacion",
        f"{BASE_URL}/categories/MCO1648"
    )

    # 4. Tendencias de búsqueda en Colombia
    results["trends"] = probe_endpoint(
        "trends",
        f"{BASE_URL}/sites/MCO/trends/search"
    )

    # 5. Detalle de un producto específico (si la búsqueda arrojó resultados)
    first_item_id = None
    search_body = results["search_keyword"].get("body", {})
    if isinstance(search_body, dict) and "results" in search_body and len(search_body["results"]) > 0:
        first_item_id = search_body["results"][0].get("id")

    if first_item_id:
        results["item_detail"] = probe_endpoint(
            f"item_{first_item_id}",
            f"{BASE_URL}/items/{first_item_id}"
        )
    else:
        results["item_detail"] = {"note": "No se pudo obtener un ID de producto de la búsqueda."}

    return results


if __name__ == "__main__":
    probe_summary = run_full_probe()
    print("\n" + "=" * 50)
    print("RESUMEN DE AUDITORÍA DE LA API DE MERCADO LIBRE:")
    for key, res in probe_summary.items():
        status = res.get("status_code", "N/A")
        works = "✅ Sí (Público)" if res.get("works_without_token") else "❌ No (Requiere Token / Bloqueado)"
        print(f"- {key}: HTTP {status} -> {works}")
    print("=" * 50)
