# 📊 Sistema de Soporte a la Toma de Decisiones para Arbitraje en Mercado Libre Colombia

**Proyecto de Grado / Emprendimiento en Ciencia de Datos**  
**Autor:** Julián Duarte  
**Universidad:** Universidad Externado de Colombia  

---

## 🎯 Visión del Proyecto
Desarrollar un sistema analítico de recomendación (*Decision Support System - DSS*) bajo el paradigma **Human-in-the-Loop**, diseñado para identificar, evaluar y clasificar oportunidades de arbitraje comercial transfronterizo.

El sistema asume el rol de **Copiloto Analítico**: monitorea el mercado local en **Mercado Libre Colombia (MCO)** y proveedores internacionales (**Amazon US** como fuente principal y **AliExpress** para productos livianos de alto margen), calcula el costo total en destino (*Landed Cost*), evalúa el riesgo cambiario (TRM) y genera **Fichas de Oportunidad** para que el emprendedor tome la decisión final de inversión con el menor riesgo y el mayor retorno.

---

## 🧭 Pilares Estratégicos

1. **Canal Central de Ventas:** Mercado Libre Colombia (reputación, logística y pasarela protegida).
2. **Canal Satélite de Atracción:** Facebook Marketplace (embudo publicitario gratuito para redirigir tráfico a Mercado Libre).
3. **Fuentes de Proveedores:**
   - **Amazon US (80%):** Membresía Prime, envíos directos gratis a Colombia en compras > $35 USD, eventos de descuentos (Prime Days, Black Friday) y originalidad garantizada de hardware.
   - **AliExpress Choice (20%):** Accesorios y herramientas ultralivianas de alto margen para el radar exploratorio.
4. **Distribución del Portafolio:**
   - **75% Núcleo Técnico (Tecnología y PC):** Memorias RAM, almacenamiento SSD NVMe, adaptadores Wi-Fi 6, monitores portátiles y componentes de alta rotación donde existe dominio técnico previo.
   - **25% Radar Exploratorio ("Cazador de Productos Estrella"):** Rastreador de oportunidades fuera del sector tecnológico con bajo peso (< 1 kg), alta brecha de precio (> 40%) y baja competencia local.
5. **Motor Cambiario (Dólar / TRM):**
   - API diaria de la TRM oficial (`datos.gov.co`) + spread bancario.
   - Cálculo de la *TRM de Quiebre* (dólar máximo tolerable antes de perder rentabilidad).
   - Indicador de timing estadístico (valle de oportunidad vs. techo de pausa).

---

## 🗂️ Estructura del Proyecto
```text
├── data/
│   ├── raw/             # Extracciones crudas de la API de Mercado Libre y Amazon
│   └── processed/       # Datasets limpios con métricas de precios y competencia
├── notebooks/           # Notebooks de exploración y prototipado
├── reports/             # Fichas de Oportunidad y resúmenes ejecutivos en Excel
├── src/                 # Módulos de extracción, cálculo de costos y alertas
│   ├── currency.py      # Motor de TRM oficial, timing y TRM de quiebre
│   ├── meli_client.py   # Extractor de datos y competencia de Mercado Libre Colombia
│   ├── calculator.py    # Calculadora de Landed Cost, comisiones e impuestos
│   └── advisory.py      # Generador de Fichas de Oportunidad para Julián
├── .gitignore           # Configuración de exclusiones Git
├── README.md            # Documentación general
├── requirements.txt     # Dependencias del proyecto en Python
└── ROADMAP.md           # Plan de desarrollo iterativo detallado (Plan Maestro)
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
