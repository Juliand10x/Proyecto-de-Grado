# 🚀 Plan Maestro de Implementación: Sistema de Arbitraje Comercial Basado en Datos
**Proyecto de Grado / Emprendimiento Tecnológico en Ciencia de Datos**  
**Autor:** Julián Duarte  
**Institución:** Universidad Externado de Colombia  
**Versión:** 2.0 (Estrategia Refinada y Aprobación)

---

## 🎯 1. Visión y Filosofía del Sistema

El proyecto consiste en el desarrollo de un **Copiloto Analítico de Arbitraje Comercial (*Human-in-the-Loop DSS*)** que identifica brechas de precio entre proveedores internacionales y el mercado local colombiano, considerando costos logísticos, comisiones de plataforma y el riesgo cambiario (TRM Dólar).

```
┌────────────────────────────────────────────────────────────────────────┐
│                   FUENTES DE PROVEEDORES (COMPRA)                      │
│  1. Amazon US (Principal: Prime Deals, Black Friday, Envío Directo)    │
│  2. AliExpress (Secundario: Accesorios ligeros de alto margen)          │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ Extracción & Análisis
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   MOTOR DE INTELIGENCIA DE DATOS                       │
│  • API Mercado Libre Colombia (Precios, volumen y competencia)         │
│  • Módulo Cambiario TRM (API Datos Abiertos + Break-Even TRM + Timing) │
│  • Modelo de Costo Puesto en Colombia (Landed Cost + Comisiones Meli)  │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ Emite
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│              FICHA DE OPORTUNIDAD ACCIONABLE (CONSEJO)                 │
│  • Producto, proveedor, precio en USD y TRM de quiebre                 │
│  • Precio sugerido en MCO, ganancia neta en COP y ROI esperado         │
│  • Calificación de riesgo (peso, fragilidad, rotación estimada)       │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ Decisión
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    JULIÁN DUARTE (DECISOR EXPERTO)                     │
│  - Aprueba la compra con base en criterio técnico                      │
│  - Publica en Mercado Libre (Canal Central)                            │
│  - Tráfico y visibilidad extra vía Facebook Marketplace (Embudo)       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🛒 2. Estrategia de Proveedores: ¿Dónde Comprar?

### A. Proveedor Principal: Amazon US (Foco 80%)
* **Por qué:** Confiabilidad absoluta en originalidad de hardware, garantía de devolución y acceso a tu membresía **Amazon Prime**.
* **Ventajas operativas:**
  1. **Envío Gratis a Colombia en compras > $35 USD:** Cientos de componentes aplican para entrega directa en Colombia sin pagar casillero.
  2. **Eventos de Descuento Agresivo:** Prime Day (Julio), Prime Big Deal Days (Octubre), Black Friday y Cyber Monday (Noviembre), donde los componentes caen entre un 20% y 45%.
  3. **Amazon Lightning Deals & Price Drops:** Descuentos flash que duran de 6 a 24 horas.
* **Sub-fuente vinculada:** **Woot.com** (sitio de liquidaciones oficiales de Amazon exclusivo para miembros Prime con descuentos de hasta el 60%).

### B. Proveedor Secundario: AliExpress Choice (Foco 20%)
* **Por qué:** Ideal para el radar de "productos estrella" fuera de tecnología y accesorios de PC ultralivianos (peso < 200g) con márgenes netos superiores al 60% (cables trenzados, tarjetas PCIe, herramientas de precisión, adaptadores).
* **Tiempos de entrega:** 10 a 18 días con envío Choice (gratis o muy económico).

---

## 🏪 3. Estrategia de Canales de Venta

1. **Mercado Libre Colombia (Canal Central y Analítico):**
   * Es el núcleo donde se consolidan ventas, reputación de vendedor, cobros protegidos por Mercado Pago y logística automatizada (Mercado Envíos).
   * La meta operativa es alcanzar las 10 ventas iniciales con calificación verde para activar el termómetro de reputación y escalar a **MercadoLíder**.
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

## 📋 6. Roadmap Detallado por Fases y Criterios de Aprobación

```
[Fase 0: Cimientos] ──> [Fase 1: Meli Radar & TRM] ──> [Fase 2: Ficha de Compra] ──> [Fase 3: Alertas] ──> [Fase 4: ML & Grado]
     (Completada)           (Siguiente Paso)               (Siguiente Venta)           (Escalamiento)         (Tesis Externado)
```

### 🔹 Fase 0: Cimientos y Configuración (Estado: ✅ COMPLETADA)
- [x] Repositorio Git vinculado a GitHub (`Juliand10x/Proyecto-de-Grado`).
- [x] Entorno virtual Python (`.venv`) y dependencias instaladas.
- [x] Estructura modular de carpetas creada.
- [x] Definición estratégica de canales y proveedores.

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

### 🔹 Fase 2: Calculadora de Costos y Generador de Fichas de Oportunidad (Duración: 2 semanas)
**Objetivo:** El sistema genera recomendaciones formales de compra para que Julián tome la decisión de su próxima importación.

- [ ] **Calculadora de Costo en Destino (`src/calculator.py`):**
  - Modelo tributario: parametrizar exención TLC / IVA 19% (< $200 USD).
  - Flete: Amazon Direct ($0 en compras elegibles) vs. casillero por libra.
  - Comisiones de Mercado Libre: comisiones por categoría (11% al 16%) + costo fijo por transacción + costo de envío gratis.
- [ ] **Generador de Ficha de Oportunidad (`src/advisory.py`):**
  - Generación de la Ficha en formato Markdown/Texto legible con:
    - Especificaciones técnicas validadas.
    - Comparativa: Precio Amazon vs. Precio sugerido MCO.
    - Utilidad neta en COP, ROI porcentual y TRM de quiebre.
    - Nivel de riesgo logístico y de rotación.
- [ ] 🎯 **Gate de Validación Comercial:** Julián revisa la Ficha, aprueba la compra de 1 o 2 productos y ejecuta la orden en Amazon aprovechando una ventana favorable de la TRM.

---

### 🔹 Fase 3: Monitoreo Continuo y Bot de Alertas (Duración: 3 semanas)
**Objetivo:** El sistema vigila ofertas 24/7 y te avisa al celular cuando hay que comprar.

- [ ] **Watchlist Tracker:**
  - Monitoreo periódico de la lista de productos preseleccionados en Amazon.
  - Detección de caídas de precio reales (evitar falsos descuentos mediante histórico).
- [ ] **Bot de Alertas (Telegram):**
  - Notificación instantánea al celular con la Ficha de Oportunidad cada vez que un producto de la Watchlist baje de precio y la TRM sea favorable.
- [ ] **Base de Datos Histórica (SQLite):**
  - Registro diario de precios de la competencia en MCO y de la TRM para análisis de series de tiempo.
- [ ] 🎯 **Gate de Validación Comercial:** Lograr al menos 3 a 5 ventas adicionales en Mercado Libre guiadas por las alertas del bot.

---

### 🔹 Fase 4: Matching Inteligente, Optimización y Documento de Grado (Duración: 4 semanas)
**Objetivo:** Completar el rigor académico de Ciencia de Datos para la sustentación en la Universidad Externado.

- [ ] **Matching Semántico de Productos (PLN):**
  - Emparejamiento de títulos de Amazon y Mercado Libre mediante similitud de texto/embeddings (Cosine Similarity) para automatizar el cruce de catálogo.
- [ ] **Algoritmo de Optimización de Capital (Knapsack Problem):**
  - Modelo de optimización matemática que recibe tu presupuesto disponible ($ COP) y genera la combinación de compra que maximiza la rentabilidad esperada.
- [ ] **Dashboard Interactivo (Streamlit):**
  - Panel web local con visualización de oportunidades, inventario activo y retorno de inversión real obtenido.
- [ ] **Documento Final de Emprendimiento / Grado:**
  - Redacción del informe final con marco teórico, metodología de ingeniería de datos, validación empírica y resultados financieros del negocio.

---

## 📌 Formato Estándar de la Ficha de Oportunidad (Ejemplo)

```text
======================================================================
🎯 FICHA DE OPORTUNIDAD #001
======================================================================
📦 PRODUCTO: Crucial RAM 16GB (1x16GB) DDR4 3200MHz SODIMM (Laptop)
🏢 PROVEEDOR: Amazon US (Vendido y enviado por Amazon)
🔗 LINK PROVEEDOR: https://amazon.com/dp/B08C5MSV8Z
💵 PRECIO EN ORIGEN: $29.99 USD
📈 TRM EFECTIVA: $3.360 COP [Estado: 🟢 Favorable - Valle Mensual]
🚚 FLETE ESTIMADO: $0 COP (Envío Gratis a Colombia en compra > $35)
💰 COSTO PUESTO EN COLOMBIA (Landed Cost): $100.766 COP

🛒 MERCADO LIBRE COLOMBIA:
   - Competidor líder: $169.900 COP (Ventas estimadas: +80 uds/mes)
   - Precio de venta sugerido: $159.900 COP
   - Comisión Meli (Clásica 13% + retenciones): $25.500 COP
   - Envío local asumido: $0 (comprador paga o incluido según rango)

📊 INDICADORES FINANCIEROS:
   - Utilidad Neta en Bolsillo: +$33.634 COP por unidad
   - Rentabilidad (ROI): 33.3%
   - TRM Máxima de Quiebre: $3.950 COP (Margen seguro ante subida del dólar)
   - Nivel de Riesgo: 🟢 MUY BAJO (Peso < 50g, no frágil, altísima rotación)

👉 CONSEJO DE INVERSIÓN:
   [COMPRA RECOMENDADA: 2 a 3 unidades] - Excelente brecha y dólar en rango óptimo.
======================================================================
```
