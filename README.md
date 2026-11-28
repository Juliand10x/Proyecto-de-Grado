# 📊 Sistema de Soporte a la Toma de Decisiones para Arbitraje en Mercado Libre Colombia

**Proyecto de Grado / Emprendimiento en Ciencia de Datos**  
**Autor:** Julián Duarte  
**Universidad:** Universidad Externado de Colombia  

---

## 🎯 Visión del Proyecto
Desarrollar un sistema analítico de recomendación (*Decision Support System - DSS*) bajo el paradigma **Human-in-the-Loop**, diseñado para identificar, comparar y evaluar oportunidades de arbitraje comercial transfronterizo hacia **Mercado Libre Colombia (MCO)**.

El sistema asume el rol de **Copiloto Analítico**: monitorea el mercado local, compara en tiempo real tiendas internacionales (**Amazon US y eBay Oficial**), normaliza costos logísticos (*Landed Cost*), evalúa el riesgo cambiario (TRM) y genera **Fichas de Oportunidad** para que el emprendedor tome decisiones de inversión fundamentadas en datos reales.

---

## 🧭 Reglas de Desarrollo Obligatorias (Ver [AGENTS.md](file:///c:/Users/sduar/Documents/Universidad/Mercado%20Libre/AGENTS.md))
1. **Una fase a la vez:** Cada fase tiene un criterio de "Listo cuando" que debe cumplirse estrictamente antes de pasar a la siguiente.
2. **Un commit por tarea terminada.**
3. **Cero credenciales en código:** Uso estricto de `.env` (ignorado en `.gitignore`).
4. **Parámetros centralizados en `config.yaml`:** Comisiones, márgenes e impuestos viven en configuración, no en código.
5. **Pruebas automáticas (`pytest`):** Cálculos financieros protegidos con suites de pruebas.
6. **Datos crudos inmutables:** Guardados con timestamp en `data/raw/` antes de cualquier transformación.

---

## 🗺️ Hoja de Ruta (Plan Maestro)
Consultar [ROADMAP.md](file:///c:/Users/sduar/Documents/Universidad/Mercado%20Libre/ROADMAP.md) para el detalle de cada fase:
* **Fase 1 (En curso):** Refuerzo de la base y exploración de la API de Mercado Libre.
* **Fase 2:** Captura diaria de Mercado Libre y de la TRM (acumulación de series de tiempo).
* **Fase 3:** Calculadora de costo puesto en Colombia, calibración con ventas reales y TRM de quiebre.
* **Fase 4:** Lado de costos (Amazon/eBay), emparejamiento curado y Ficha de Oportunidad.
* **Fase 5:** Panel en Streamlit, alertas en Telegram y reglas del dólar con backtesting.
* **Fase 6:** Automatización progresiva, nuevos proveedores y ampliación de catálogo.

---

## 🗂️ Estructura del Repositorio
```text
├── config.yaml          # Parámetros de negocio (comisiones, márgenes, costos)
├── requirements.txt     # Dependencias de Python
├── ROADMAP.md           # Plan maestro de implementación por fases
├── README.md            # Documentación general del repositorio
├── AGENTS.md            # Reglas de desarrollo y directrices técnicas
├── .env.example         # Plantilla de variables de entorno
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
└── tests/               # Pruebas unitarias automatizadas con pytest
```

---

## 🚀 Instalación y Puesta en Marcha

1. **Activar el entorno virtual:**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. **Instalar dependencias actualizadas:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Ejecutar pruebas unitarias:**
   ```powershell
   pytest
   ```
