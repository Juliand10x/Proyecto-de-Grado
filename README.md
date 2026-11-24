# 📊 Sistema de Soporte a la Toma de Decisiones para Arbitraje en Mercado Libre Colombia

**Proyecto de Grado / Emprendimiento en Ciencia de Datos**  
**Autor:** Julián Duarte  
**Universidad:** Universidad Externado de Colombia  

---

## 🎯 Visión del Proyecto
Desarrollar un sistema analítico de recomendación (*Decision Support System - DSS*) bajo el paradigma **Human-in-the-Loop**, diseñado para identificar, evaluar y clasificar oportunidades de arbitraje comercial transfronterizo.

El sistema asume el rol de **Copiloto Analítico**: monitorea el mercado local en **Mercado Libre Colombia (MCO)** y proveedores internacionales (Amazon, AliExpress, etc.), calcula el costo total en destino (*Landed Cost*) y genera **Fichas de Oportunidad** para que el emprendedor tome la decisión final de inversión con el menor riesgo y el mayor retorno.

---

## 🧭 Pilares Estratégicos

1. **Canal Central de Ventas:** Mercado Libre Colombia.
2. **Canal Satélite de Atracción:** Facebook Marketplace (utilizado exclusivamente como embudo de visibilidad orgánica hacia Mercado Libre).
3. **Distribución del Portafolio:**
   - **75% Núcleo Técnico (Tecnología y PC):** Memorias RAM, almacenamiento SSD NVMe, adaptadores Wi-Fi 6, monitores portátiles y componentes de alta rotación donde existe dominio técnico previo.
   - **25% Radar Exploratorio ("Cazador de Productos Estrella"):** Rastreador de oportunidades fuera del sector tecnológico (herramientas de precisión, audio de nicho, cuidado personal) con bajo peso, alta brecha de precio y baja competencia local.

---

## 🗂️ Estructura del Proyecto
```text
├── data/
│   ├── raw/             # Extracciones crudas de la API de Mercado Libre y Amazon
│   └── processed/       # Datasets limpios con métricas de precios y competencia
├── notebooks/           # Notebooks de exploración y prototipado
├── reports/             # Fichas de Oportunidad y resúmenes ejecutivos en Excel
├── src/                 # Módulos de extracción, cálculo de costos y alertas
├── .gitignore           # Configuración de exclusiones Git
├── README.md            # Documentación general
├── requirements.txt     # Dependencias del proyecto en Python
└── ROADMAP.md           # Plan de desarrollo iterativo detallado
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
