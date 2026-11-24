# 📊 Sistema de Soporte a la Toma de Decisiones para Arbitraje en Mercado Libre Colombia

**Proyecto de Grado / Emprendimiento en Ciencia de Datos**  
**Autor:** Julián Duarte  
**Universidad:** Universidad Externado de Colombia  

---

## 🎯 Visión del Proyecto
Desarrollar un sistema analítico de recomendación (*Decision Support System - DSS*) bajo el paradigma **Human-in-the-Loop**, diseñado para identificar, comparar y evaluar oportunidades de arbitraje comercial transfronterizo a través de un **motor multi-proveedor**.

El sistema asume el rol de **Copiloto Analítico**: monitorea el mercado local en **Mercado Libre Colombia (MCO)** y compara en tiempo real múltiples tiendas internacionales (**Amazon US, Newegg, AliExpress, eBay Refurbished, Woot, B&H**), normaliza costos logísticos (*Landed Cost*), evalúa el riesgo cambiario (TRM) y genera **Fichas de Comparación Multi-Proveedor** para que el emprendedor elija la opción de compra que maximice el ROI y minimice el tiempo de rotación.

---

## 🧭 Pilares Estratégicos

1. **Canal Central de Ventas:** Mercado Libre Colombia (reputación, logística y pasarela protegida).
2. **Canal Satélite de Atracción:** Facebook Marketplace (embudo publicitario gratuito para captar y dirigir compradores a Mercado Libre).
3. **Matriz Multi-Proveedor:**
   - **Amazon US:** Envío directo gratis a Colombia (> $35 USD), Prime Deals, originalidad garantizada.
   - **Newegg:** Especialista en hardware de PC, combos y ofertas *Shell Shocker*.
   - **AliExpress Choice:** Accesorios ultralivianos de alto margen y radar de productos estrella.
   - **eBay (Top-Rated / Refurbished):** Monitores y liquidaciones con garantía oficial de fabricante.
   - **Woot! / B&H Photo Video:** Liquidaciones de Amazon y ofertas de open-box.
4. **Distribución del Portafolio:**
   - **75% Núcleo Técnico (Tecnología y PC):** Memorias RAM, almacenamiento SSD NVMe, adaptadores Wi-Fi 6, monitores portátiles y periféricos gamer.
   - **25% Radar Exploratorio ("Cazador de Productos Estrella"):** Productos fuera de tecnología con bajo peso (< 1 kg), alta brecha de precio (> 40%) y baja competencia local.
5. **Motor Cambiario (Dólar / TRM):**
   - API diaria de la TRM oficial (`datos.gov.co`) + spread bancario.
   - Cálculo de la *TRM de Quiebre* (dólar máximo tolerable antes de perder rentabilidad).
   - Indicador de timing estadístico (valle de oportunidad vs. techo de pausa).

---

## 🗂️ Estructura del Proyecto
```text
├── data/
│   ├── raw/             # Extracciones crudas de Meli y proveedores externos
│   └── processed/       # Datasets limpios con métricas de precios y competencia
├── notebooks/           # Notebooks de exploración y prototipado
├── reports/             # Fichas de Oportunidad y resúmenes ejecutivos en Excel
├── src/                 # Módulos de extracción, cálculo de costos y alertas
│   ├── currency.py      # Motor de TRM oficial, timing y TRM de quiebre
│   ├── meli_client.py   # Extractor de datos y competencia de Mercado Libre Colombia
│   ├── calculator.py    # Calculadora de Landed Cost, comisiones e impuestos
│   ├── sourcing.py      # Comparador multi-proveedor (Amazon, Newegg, AliExpress, etc.)
│   └── advisory.py      # Generador de Fichas de Oportunidad para Julián
├── .gitignore           # Configuración de exclusiones Git
├── README.md            # Documentación general
├── requirements.txt     # Dependencias del proyecto en Python
└── ROADMAP.md           # Plan Maestro de Implementación detallado
```

---

## 🚀 Entorno de Desarrollo

1. **Activar el entorno virtual:**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. **Instalar dependencias:**
   ```powershell
   pip install -r requirements.txt
   ```
