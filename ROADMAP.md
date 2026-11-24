# 🚀 Plan Maestro de Implementación: Sistema de Arbitraje Comercial Basado en Datos
**Proyecto de Grado / Emprendimiento Tecnológico en Ciencia de Datos**  
**Autor:** Julián Duarte  
**Institución:** Universidad Externado de Colombia  
**Versión:** 3.0 (Motor Multi-Proveedor y Optimización de Sourcing)

---

## 🎯 1. Visión y Filosofía del Sistema

El proyecto consiste en el desarrollo de un **Copiloto Analítico de Arbitraje Comercial Multi-Proveedor (*Multi-Source DSS*)**. 

A diferencia de un modelo que depende de una sola tienda, este sistema monitorea de manera simultánea una **red de proveedores internacionales**, normaliza los costos de importación de cada uno y determina **cuál proveedor ofrece la mayor rentabilidad neta real** al vender el producto en **Mercado Libre Colombia (MCO)**.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      MATRIZ DE PROVEEDORES INTERNACIONALES                      │
│   [Amazon US]     [Newegg]     [AliExpress]     [eBay Refurbished]     [Woot]   │
│   Precios/Deals  Hardware/Combos Choice/Cupones   Liquidaciones      Open-Box   │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │ Normalización de Precios & Fletes
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     MOTOR DE INTELIGENCIA Y COMPARACIÓN                         │
│  • API Mercado Libre Colombia (Precios, volumen y competencia)                  │
│  • Módulo Cambiario TRM (API Datos Abiertos + Break-Even TRM + Timing)          │
│  • Comparador de Landed Cost (Calcula flete, arancel y comisiones por proveedor)│
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │ Genera Ranking de Rentabilidad
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                 FICHA DE COMPARACIÓN MULTI-PROVEEDOR                            │
│  Para el producto X:                                                            │
│  - Proveedor A: Costo $34 USD ➔ Margen 21% (Entrega: 5 días)                    │
│  - Proveedor B: Costo $28 USD ➔ Margen 32% (Entrega: 8 días) 🏆 GANADOR        │
│  - Proveedor C: Costo $25 USD ➔ Margen 38% (Entrega: 18 días / Mayor riesgo)   │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │ Decisión
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      JULIÁN DUARTE (DECISOR EXPERTO)                            │
│  - Selecciona la opción más conveniente según balance de Margen vs. Tiempo      │
│  - Ejecuta la compra y publica en Mercado Libre (Canal Central)                 │
│  - Promueve vía Facebook Marketplace (Embudo publicitario satélite)             │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🌐 2. La Red de Proveedores Internacionales

El sistema comparará ofertas entre las siguientes plataformas según la categoría:

| Proveedor | Especialidad | Modelo de Flete / Logística | Fortaleza Principal |
| :--- | :--- | :--- | :--- |
| **Amazon US** | Hardware de marca, periféricos, monitores | Envío gratis a Colombia (> $35 USD) o casillero | Velocidad, Prime Deals, originalidad 100% garantizada. |
| **Newegg** | Componentes de PC (RAM, SSD, GPUs, Placas) | Casillero en Miami | Ofertas *Shell Shocker*, combos de hardware y precios mayoristas. |
| **AliExpress (Choice)** | Accesorios livianos, adaptadores, herramientas, gadgets | Envío directo Choice a Colombia (gratis o < $2 USD) | Márgenes altísimos (60% a 150%) en el radar de productos estrella. |
| **eBay (Top-Rated / Certified Refurbished)** | Monitores, laptops, hardware empresarial | Casillero en Miami | Liquidaciones y reacondicionados oficiales con garantía de 1-2 años a mitad de precio. |
| **Woot! (Amazon Liquidations)** | Electrónica y gadgets en remate | Casillero o Prime US | Descuentos agresivos de liquidación (40% al 70%). |
| **B&H Photo Video** | Monitores especializados, almacenamiento, audio | Envío directo DHL/FedEx o casillero | Descuentos de temporada y sección *Used/Open-Box*. |

---

## 🏪 3. Estrategia de Canales de Venta

1. **Mercado Libre Colombia (Canal Central y Analítico):**
   * Es el núcleo donde se consolidan ventas, reputación de vendedor, cobros protegidos por Mercado Pago y logística automatizada (Mercado Envíos).
   * Meta: alcanzar el estatus de **MercadoLíder** para ganar algoritmo y visibilidad orgánica preferencial.
2. **Facebook Marketplace (Canal Satélite de Publicidad):**
   * Se utiliza únicamente como **embudo de atracción gratuito (Top of Funnel)**.
   * Se listan los productos localmente para captar clientes y se les ofrece el enlace de Mercado Libre para que compren con tranquilidad, cuotas y envío asegurado.

---

## 💵 4. El Motor Cambiario (Dólar / TRM)

Para proteger la rentabilidad y saber **cuándo comprar y cuándo esperar**:
1. **API Oficial de la TRM:** Conexión diaria con la API del Banco de la República / Superfinanciera (`datos.gov.co`) + cálculo de TRM efectiva bancaria (+2% de spread).
2. **TRM de Quiebre (*Break-Even TRM*):** Cálculo automático del dólar máximo tolerable para que un producto mantenga un margen neto mínimo del 20%. Si el dólar supera ese valor, la oportunidad se descarta.
3. **Indicador de Timing (Z-Score & Medias Móviles):**
   * **🔴 Techo mensual (Dólar caro):** Congelar compras de bajo margen; esperar retroceso.
   * **🟢 Valle mensual (Dólar barato):** Ventana verde para comprar stock de la Watchlist.

---

## 📦 5. Portafolio de Inversión

* **75% Núcleo Técnico (Tecnología & PC):**
  * Memorias RAM (DDR4 / DDR5 para laptop y desktop).
  * Almacenamiento SSD M.2 NVMe (Gen 3 y Gen 4 de 1TB y 2TB).
  * Adaptadores de red Wi-Fi 6E / Bluetooth 5.3 PCIe y USB.
  * Monitores portátiles USB-C (15.6" IPS 1080p).
  * Periféricos gamer específicos de alta demanda y bajo peso.
* **25% Radar "Cazador de Productos Estrella":**
  * Productos fuera de tecnología detectados por tendencias en Mercado Libre Colombia que cumplan: *Peso < 1 kg + Brecha internacional/local > 40% + Poca o mala competencia local*.

---

## 📋 6. Roadmap Detallado por Fases

```
[Fase 0: Cimientos] ──> [Fase 1: Meli Radar & TRM] ──> [Fase 2: Comparador Multi-Proveedor] ──> [Fase 3: Alertas] ──> [Fase 4: ML & Grado]
     (Completada)           (Siguiente Paso)                    (Siguiente Venta)              (Escalamiento)        (Tesis Externado)
```

### 🔹 Fase 0: Cimientos y Configuración (Estado: ✅ COMPLETADA)
- [x] Repositorio Git vinculado a GitHub (`Juliand10x/Proyecto-de-Grado`).
- [x] Entorno virtual Python (`.venv`) y dependencias instaladas.
- [x] Estructura modular de carpetas creada.
- [x] Definición estratégica de canales y arquitectura multi-proveedor.

---

### 🔹 Fase 1: Meli Radar & Motor Cambiario (Duración: 1 - 2 semanas)
**Objetivo:** Tener funcionando los extractores de datos locales y el monitor del dólar en tiempo real.

- [ ] **Módulo Cambiario (`src/currency.py`):**
  - Conectar a la API de datos abiertos de Colombia para descargar la TRM oficial diaria.
  - Calcular medias móviles (20 y 50 días) y clasificar el estado del dólar (🟢 Valle / 🟡 Normal / 🔴 Techo).
  - Función de cálculo de TRM efectiva bancaria.
- [ ] **Módulo Extractor de Mercado Libre (`src/meli_client.py`):**
  - Conectar a la API pública de Mercado Libre Colombia (`/sites/MCO/search`).
  - Extractor para categorías de PC (Memorias RAM, SSDs, Monitores).
  - Cálculo de métricas: Precio mínimo competitivo, precio mediana, competidores con envío Full y ventas acumuladas (`sold_quantity`).
- [ ] **Módulo Radar de Tendencias (`src/trends_scanner.py`):**
  - Consulta automática de `/sites/MCO/trends` para identificar palabras clave con crecimiento en Colombia fuera del sector de tecnología.
- [ ] **Salida:** Reporte en Excel / DataFrame listo para usar.
- [ ] 🎯 **Gate de Validación Comercial:** Identificar con datos reales 2 productos de hardware y 1 fuera de tecnología con alta demanda local.

---

### 🔹 Fase 2: Motor de Comparación Multi-Proveedor y Fichas de Oportunidad (Duración: 2 semanas)
**Objetivo:** El sistema cruza un producto objetivo contra múltiples tiendas internacionales y entrega la mejor opción de compra.

- [ ] **Normalizador de Costos Multi-Proveedor (`src/calculator.py`):**
  - Flete adaptativo según proveedor: Amazon Direct ($0 en elegibles) vs. Casillero por libra (Newegg, eBay, B&H) vs. Envío Choice (AliExpress).
  - Impuestos Colombia (TLC < $200 USD / IVA parametrizado).
  - Comisiones de Mercado Libre por categoría (11% al 16%) + costo de envío asumido.
- [ ] **Módulo Comparador de Proveedores (`src/sourcing.py`):**
  - Entrada: Modelo de producto (ej. `Crucial P3 1TB NVMe PCIe 3.0`).
  - Consulta precios en Amazon, Newegg, AliExpress y eBay.
  - Salida: Tabla comparativa ordenada por **Margen Neto Final ($ y %)**.
- [ ] **Generador de Ficha de Recomendación:**
  - Emisión de la ficha ejecutiva para que Julián escoja el proveedor ganador y ejecute la compra.
- [ ] 🎯 **Gate de Validación Comercial:** Julián revisa la comparativa multi-proveedor, escoge la fuente más rentable y realiza una compra real.

---

### 🔹 Fase 3: Monitoreo Continuo y Bot de Alertas (Duración: 3 semanas)
**Objetivo:** El sistema vigila ofertas en todos los proveedores y te avisa al celular cuando haya una oportunidad clara.

- [ ] **Watchlist Tracker Multi-Sitio:**
  - Rastreo periódico de la lista de productos preseleccionados en las diferentes tiendas.
- [ ] **Bot de Alertas (Telegram):**
  - Notificación instantánea al celular: *"¡Alerta de Arbitraje! El producto X está en oferta en [Proveedor Ganador] con un 31% de margen neto en Mercado Libre"*.
- [ ] **Base de Datos Histórica (SQLite):**
  - Registro de precios de cada tienda para detectar caídas de precio históricas.
- [ ] 🎯 **Gate de Validación Comercial:** Lograr al menos 3 a 5 ventas adicionales en Mercado Libre guiadas por las alertas del bot.

---

### 🔹 Fase 4: Matching Inteligente, Optimización y Documento de Grado (Duración: 4 semanas)
**Objetivo:** Completar el rigor académico de Ciencia de Datos para la sustentación en la Universidad Externado.

- [ ] **Matching Semántico de Productos (PLN):**
  - Emparejamiento de títulos de diferentes tiendas mediante similitud de texto/embeddings (Cosine Similarity) para automatizar el cruce de catálogos multitienda.
- [ ] **Algoritmo de Optimización de Capital (Knapsack Problem):**
  - Modelo matemático que asigna presupuesto entre proveedores para maximizar el ROI de la canasta de compras.
- [ ] **Dashboard Interactivo (Streamlit):**
  - Panel web local con visualización de oportunidades por proveedor, inventario activo y retorno real.
- [ ] **Documento Final de Emprendimiento / Grado:**
  - Redacción del informe final con marco teórico, metodología de ingeniería de datos, validación empírica y resultados financieros del negocio.

---

## 📌 Ejemplo: Ficha de Comparación Multi-Proveedor

```text
================================================================================
🎯 FICHA DE COMPARACIÓN MULTI-PROVEEDOR #002
================================================================================
📦 PRODUCTO: SSD M.2 NVMe Crucial P3 Plus 1TB PCIe 4.0 (Hasta 5000 MB/s)
🛒 PRECIO OBJETIVO MERCADO LIBRE COLOMBIA:
   - Competidor líder: $349.900 COP (Ventas acumuladas: +200 uds)
   - Precio de venta sugerido: $329.900 COP
   - Comisiones Meli + Envío local: $54.200 COP
   - Ingreso Neto en Mercado Libre: $275.700 COP

📊 COMPARATIVA DE PROVEEDORES (Cálculo puesto en Colombia a TRM $3.360):
┌──────────────┬─────────────┬──────────────┬──────────────┬──────────────┬────────────┐
│ Proveedor    │ Precio USD  │ Flete Est.   │ Costo Total  │ Ganancia ($) │ ROI Neto   │
├──────────────┼─────────────┼──────────────┼──────────────┼──────────────┼────────────┤
│ 🏆 Newegg    │ $53.99 USD  │ $16.000 (Cas)│ $197.406 COP │ +$78.294 COP │  39.6%     │
│ 🥈 Amazon US │ $59.99 USD  │ $0 (Directo) │ $201.566 COP │ +$74.134 COP │  36.8%     │
│ 🥉 AliExpress│ $58.50 USD  │ $0 (Choice)  │ $196.560 COP │ +$79.140 COP │  40.2% *   │
└──────────────┴─────────────┴──────────────┴──────────────┴──────────────┴────────────┘
* Nota AliExpress: Mayor tiempo de entrega (16 días vs. 5 días en Amazon/Newegg).

👉 RECOMENDACIÓN DEL COPILOTO:
   [PROVEEDOR RECOMENDADO: NEWEGG o AMAZON]
   - Newegg ofrece el mejor balance de precio y entrega rápida a casillero en Miami.
   - Amazon es la alternativa si deseas entrega directa sin gestión de casillero por solo $4.000 COP de diferencia en margen.
================================================================================
```
