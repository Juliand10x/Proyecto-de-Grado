# 🚀 Plan de Desarrollo Iterativo: Arbitraje de E-Commerce Basado en Datos
**Proyecto de Grado / Emprendimiento Tecnológico**  
**Autor:** Julián Duarte  
**Carrera:** Ciencia de Datos – Universidad Externado de Colombia  

---

## 🎯 Filosofía del Proyecto: *Human-in-the-Loop + Lean Analytics*
El objetivo no es reemplazar tu criterio con un bot ciego de compra automática, sino construir un **Copiloto Analítico de Inversión**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SISTEMA ANALÍTICO (EL MOTOR)                         │
│  - Escaneo de Mercado Libre Colombia (MCO)                            │
│  - Monitoreo de proveedores (Amazon, AliExpress, etc.)                 │
│  - Cálculo de Landed Cost, Comisiones y Margen Neto                    │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ Genera
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│               FICHA DE OPORTUNIDAD (RECOMENDACIÓN CLARA)               │
│  • Producto exacto y especificaciones técnicas                         │
│  • Dónde comprar, cuándo y precio actual vs. histórico                 │
│  • Precio sugerido de venta en Meli Colombia                           │
│  • Margen neto en COP ($), ROI (%) y estimación de rotación           │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ Evalúa y Decide
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                  JULIÁN DUARTE (EL DECISOR EXPERTO)                    │
│  - Valida calidad técnica y garantías                                  │
│  - Ejecuta la compra internacional                                     │
│  - Lista en Mercado Libre (con tráfico satélite en Marketplace)        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🧭 Estrategia Comercial y de Canales

1. **Canal Central: Mercado Libre Colombia (MCO)**
   - Todo el modelo transaccional, de reputación, envíos seguros (Mercado Envíos) y cobros (Mercado Pago) se centraliza en Mercado Libre.
   - El objetivo es alcanzar el estatus de **MercadoLíder** para ganar algoritmo y visibilidad orgánica preferencial.
2. **Canal Satélite de Tráfico: Facebook Marketplace**
   - Se utiliza como canal de **publicidad gratuita y atracción (Top of Funnel)**.
   - Se publican los productos para captar compradores locales y dirigirlos a la publicación de Mercado Libre para concretar la compra con garantía y envío seguro.

---

## 📦 Estrategia de Portafolio: 75% Especialidad / 25% Exploratorio

* **Núcleo Técnico (75% del capital): Tecnología y PC**
  - Componentes de alto valor y bajo volumen/peso: Memorias RAM (DDR4/DDR5), Almacenamiento SSD NVMe, adaptadores de red Wi-Fi 6/6E, procesadores, monitores portátiles y periféricos específicos.
  - *Ventaja competitiva:* Tu conocimiento de especificaciones, compatibilidades y estándares de hardware.
* **Radar Exploratorio (25% del capital): "Cazador de Productos Estrella"**
  - Algoritmo que monitorea categorías ajenas a tecnología (herramientas de precisión, hogar inteligente, audio Hi-Fi, cuidado personal especializado).
  - Criterio de búsqueda: **Alta brecha de precio (arbitraje > 40%) + Peso liviano (< 1 kg) + Competencia local deficiente o con calificaciones bajas**.

---

## 📅 Roadmap por Fases

### 🔹 Fase 0: Fundamentos y Entorno de Trabajo (Semana 1)
- [x] Configuración de entorno Python (`.venv`) y dependencias instaladas.
- [x] Estructura modular del proyecto (`data/`, `src/`, `notebooks/`, `reports/`).
- [ ] Configuración de Git y repositorio en GitHub (`Juliand10x/Proyecto-de-Grado`).
- [ ] Definir formato estándar de la **Ficha de Oportunidad** (reporte de compra).

---

### 🔹 Fase 1: Meli Radar MVP – Inteligencia de Mercado Local (Semanas 2 - 3)
**Objetivo:** Saber exactamente qué se busca, quién vende y a qué precio en Mercado Libre Colombia.

- [ ] **Módulo 1: Extractor MCO (Tecnología & PC)**
  - Conexión a la API oficial de Mercado Libre (`/sites/MCO/search`).
  - Extracción de precios, condición, reputación de vendedores, presencia de Mercado Envíos Full y volumen histórico (`sold_quantity`).
- [ ] **Módulo 2: Radar de Tendencias y Categorías (Explorador Fuera de Tecnología)**
  - Extracción de tendencias (`/sites/MCO/trends`) y categorías con mayor crecimiento en Meli Colombia para cazar productos estrella.
- [ ] **Generador de Reportes de Mercado:**
  - Exportación a Excel/CSV con métricas clave: precio promedio, precio piso de la competencia y volumen estimado mensual.

---

### 🔹 Fase 2: Calculadora Financiera y Ficha de Oportunidad (Semanas 4 - 5)
**Objetivo:** Tener el cálculo financiero exacto y la primera versión de la Ficha de Consejo para Julián.

- [ ] **Modelo Matemático de Costo en Destino (*Landed Cost*):**
  - Flete internacional (por libra de casillero o Amazon Direct).
  - Impuestos Colombia (TLC < $200 USD / IVA 19% parametrizado).
  - TRM del día + comisión bancaria/tarjeta.
  - Comisión de Mercado Libre por categoría (11% al 16%) + costo fijo por unidad + costo de envío gratis asumido.
- [ ] **Generador de Ficha de Recomendación:**
  - Script que recibe un link de Amazon/proveedor y el producto de Meli y genera un resumen ejecutivo claro para que Julián decida si compra o no.
- [ ] **Validación con Venta Real:**
  - Ejecutar 1 o 2 compras reales respaldadas 100% por esta calculadora.

---

### 🔹 Fase 3: Monitor Continuo y Notificaciones a Julián (Semanas 6 - 8)
**Objetivo:** El sistema monitorea en segundo plano y te envía los consejos directo a tu celular.

- [ ] **Canal de Comunicación (Bot de Telegram / Discord):**
  - Notificaciones en tiempo real cuando un componente de PC o producto estrella baje de precio en EE.UU. y mantenga buen margen en Meli.
- [ ] **Base de datos de seguimiento (SQLite / PostgreSQL):**
  - Histórico de precios para saber cuándo un producto está realmente en su mínimo histórico (evitar falsos descuentos).

---

### 🔹 Fase 4: Machine Learning, Optimización y Documento de Grado (Semanas 9+)
**Objetivo:** Consolidar el rigor académico de Ciencia de Datos para la sustentación en la Universidad Externado.

- [ ] **Matching Semántico con PLN:**
  - Emparejamiento automático de publicaciones de Amazon y Mercado Libre mediante similitud de texto/embeddings.
- [ ] **Optimización de Presupuesto (Problema de la Mochila / Knapsack):**
  - Algoritmo que recibe: `Capital disponible ($ COP)` y genera la distribución óptima de compra (ej. 3 RAMs + 2 SSDs + 1 Producto Estrella).
- [ ] **Dashboard en Streamlit:**
  - Panel interactivo con histórico de ventas, inventario activo y catálogo de oportunidades.
- [ ] **Documento Final de Grado:**
  - Marco teórico, metodología de ingeniería de datos, validación empírica y resultados financieros reales del emprendimiento.
