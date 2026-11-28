# Contexto del Proyecto y Reglas de Desarrollo (AGENTS.md)

Este documento define las reglas de ingeniería, el stack tecnológico y las directrices operativas que deben seguir todos los agentes y desarrolladores que trabajen en este repositorio.

---

## 📌 Reglas de Trabajo Obligatorias

1. **Una fase a la vez:** Cada fase del [ROADMAP.md](file:///c:/Users/sduar/Documents/Universidad/Mercado%20Libre/ROADMAP.md) debe cumplir su criterio de "Listo cuando" antes de iniciar la siguiente.
2. **Un commit en Git por tarea terminada:** Mensajes claros con formato convencional (`feat:`, `fix:`, `docs:`, `test:`).
3. **Cero credenciales en código:** Ninguna clave, token o secreto se escribe en el código. Todo se lee desde `.env` mediante `python-dotenv`. `.env` DEBE permanecer ignorado en `.gitignore`.
4. **Parámetros de negocio centralizados:** Comisiones de Mercado Libre, margen mínimo objetivo, sobrecostos bancarios de tarjeta, fletes y tarifas tributarias se configuran en `config.yaml`.
5. **Pruebas automáticas obligatorias en cálculos financieros:** Toda función que calcule costos, márgenes, TRM de quiebre o comisiones debe contar con pruebas unitarias en `tests/` ejecutadas con `pytest`.
6. **Integridad de datos crudos:** Todo dato extraído de APIs o scraping se guarda intacto en `data/raw/` con timestamp ISO antes de procesarlo o limpiarlo.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.11+
* **Almacenamiento:** SQLite (`data/meli.db`) con SQLAlchemy o `sqlite3` estándar.
* **Extracción y APIs:** `requests`, `urllib3`.
* **Procesamiento de Datos:** `pandas`, `numpy`.
* **Pruebas Unitarias:** `pytest`.
* **Configuración:** `pyyaml`, `python-dotenv`.
* **Dashboard y Visualización:** `streamlit`, `matplotlib`, `seaborn`.

---

## 🗂️ Estructura del Repositorio

```text
├── config.yaml          # Parámetros de negocio (comisiones, márgenes, costos)
├── requirements.txt     # Dependencias de Python
├── ROADMAP.md           # Plan maestro de implementación por fases
├── README.md            # Documentación general del repositorio
├── AGENTS.md            # Reglas de desarrollo y directrices técnicas
├── .env.example         # Plantilla de variables de entorno (sin secretos)
├── .gitignore           # Archivos y carpetas excluidas de Git
├── data/
│   ├── raw/             # Respuestas crudas con timestamp (JSON, CSV)
│   ├── processed/       # Datasets limpios
│   └── meli.db          # Base de datos SQLite
├── docs/                # Documentación técnica y hallazgos de APIs
│   └── api_meli_hallazgos.md
├── notebooks/           # Notebooks Jupyter para experimentación y auditoría
├── reports/             # Fichas de oportunidad y reportes ejecutivos
├── src/                 # Código fuente modular
│   ├── __init__.py
│   ├── meli_client.py   # Cliente de la API de Mercado Libre
│   ├── currency.py      # Motor de TRM oficial y series de tiempo
│   ├── costing.py       # Modelo financiero de Landed Cost y TRM de quiebre
│   ├── sourcing.py      # Conectores a proveedores (Amazon, eBay)
│   └── opportunities.py # Generador de Fichas de Oportunidad
└── tests/               # Pruebas unitarias automatizadas con pytest
```

---

## 🏛️ Esquema de la Base de Datos (`data/meli.db`)

* `ml_listings`: Publicaciones capturadas de Mercado Libre (id, título, categoría, precio, vendedor, reputación, full, sold_quantity, timestamp).
* `source_products`: Catálogo de productos vigilados en proveedores externos (Amazon, eBay).
* `product_matches`: Equivalencias curadas manualmente entre Meli y proveedores.
* `fx_rates`: Histórico diario de la TRM oficial de Colombia.
* `opportunities`: Oportunidades detectadas, márgenes proyectados y estado de aprobación de Julián.
* `orders`: Registro de compras reales realizadas y sus costos efectivos para calibración.
