# 🚀 Plan Maestro de Implementación: Arbitraje Comercial Basado en Datos
**Proyecto de Grado / Emprendimiento Tecnológico en Ciencia de Datos**  
**Autor:** Julián Duarte  
**Institución:** Universidad Externado de Colombia  
**Versión:** 4.0 (Plan Reajustado por Fases y Criterios de Aceptación)

---

## 📌 Reglas de Trabajo (Valen para todas las fases)

1. **Una fase a la vez, y cada fase termina con su criterio de "listo" cumplido** antes de pasar a la siguiente.
2. **Un commit en Git por tarea terminada.**
3. **Nada de claves en el código.** Todo va en `.env`, y `.env` debe estar en `.gitignore`.
4. **Los parámetros de negocio viven en un archivo de configuración** (`config.yaml`), no dentro del código: comisión de Mercado Libre, margen mínimo, sobrecosto de tarjeta, costos de courier, impuestos.
5. **Las fórmulas de dinero llevan pruebas automáticas** (`pytest`). Un error ahí cuesta plata real.
6. **Los datos crudos se guardan antes de limpiarlos**, siempre con fecha y hora en `data/raw/`.

---

## 🔹 Fase 1: Refuerzo de la base y exploración de la API de Mercado Libre

* **Objetivo:** Dejar la base lista para acumular datos y averiguar qué entrega realmente la API de Mercado Libre Colombia.
* **Por qué va primero:** Todo el proyecto depende de datos de Mercado Libre, y el plan original asumía que ciertos campos existían sin verificarlo. Mejor descubrir ahora lo que no se puede obtener.

### Qué se construye:
- `AGENTS.md` con el contexto del proyecto, el stack y las reglas de trabajo.
- Base de datos **SQLite** (`data/meli.db`) y esquema inicial de tablas:
  - `ml_listings` (publicaciones capturadas de Mercado Libre)
  - `source_products` (catálogo de productos vigilados en proveedores externos)
  - `product_matches` (equivalencias curadas entre Meli y proveedores)
  - `fx_rates` (histórico diario de la TRM oficial)
  - `opportunities` (cálculos de margen y alertas generadas)
  - `orders` (registro de compras e importaciones reales)
- `config.yaml` con los parámetros de negocio.
- Carpeta `tests/` con `pytest` configurado.
- `notebooks/01_exploracion_api_meli.ipynb`.

### Cómo se hace:
1. Crear la aplicación en el portal de desarrolladores de Mercado Libre y guardar las credenciales en `.env`.
2. Verificar que `.env` esté en `.gitignore` y que ningún secreto esté ya en GitHub.
3. Probar **cada endpoint por separado** (búsqueda por categoría, detalle de un producto, tendencias, información del vendedor) y anotar para cada uno: si funciona sin token, qué campos devuelve y cuáles vienen vacíos.
4. Revisar en especial si `sold_quantity` llega exacto o en rangos, y si la reputación del vendedor y la logística Full están disponibles.
5. Guardar un ejemplo de respuesta cruda de cada endpoint en `data/raw/`.
6. Escribir un documento corto `docs/api_meli_hallazgos.md` con lo que sí y lo que no se puede obtener.

* **Listo cuando:** Tienes el documento de hallazgos y sabes con certeza si la captura será por API, por scraping o mixta.
* **Decisión que depende de esta fase:** Si algún dato clave no está en la API, se decide si se obtiene por scraping (con sus riesgos de bloqueo) o si se cambia la variable analizada.

---

## 🔹 Fase 2: Captura diaria de Mercado Libre y de la TRM

* **Objetivo:** Empezar a acumular series de tiempo, que es el activo de datos más valioso del proyecto.
* **Por qué aquí:** Los datos de Mercado Libre de hoy no se pueden recuperar mañana. La TRM sí se puede recuperar históricamente, pero conviene dejarla automatizada.

### Qué se construye:
- `src/meli_client.py`: Cliente de la API (autenticación, reintentos, manejo de errores, rate limits).
- `src/collect_meli.py`: Script de captura por categoría.
- `src/currency.py`: Descarga de la TRM oficial desde datos abiertos (`datos.gov.co`), incluyendo historial completo.
- Programador de tareas (cron o APScheduler) que lo ejecute cada día.

### Cómo se hace:
1. Empezar con **una sola categoría: memorias RAM**. (Razón: categoría pequeña y con especificaciones estandarizadas que permite auditar datos a mano rápido).
2. Cada captura guarda: ID de publicación, título, categoría, precio, vendedor, reputación, logística, ventas acumuladas (según Fase 1) y timestamp. **No se sobrescribe nada.**
3. Cargar el historial de la TRM y programar la captura diaria.
4. Agregar registro de errores (`logging`) para monitorear ejecuciones fallidas.
5. Cuando funcione de forma estable con RAM, agregar SSDs y monitores.

* **Listo cuando:** El sistema corre solo durante 5 días seguidos sin intervención y la base de datos tiene capturas diarias coherentes.

---

## 🔹 Fase 3: Calculadora de costo puesto en Colombia y TRM de quiebre

* **Objetivo:** Que el sistema calcule con precisión cuánto cuesta realmente un producto puesto en destino y cuánto margen neto deja.
* **Por qué aquí:** Es el corazón financiero del proyecto. El punto de quiebre del dólar no se puede calcular sin esta calculadora; va antes que cualquier señal cambiaria.

### La Fórmula Financiera:
* **Utilidad neta:**
  $$U = P \cdot (1 - c) - F - O - K \cdot \text{TRM}_{\text{ef}}$$
* **Margen neto:**
  $$M = \frac{U}{P}$$
* **TRM Efectiva de Quiebre** (dólar efectivo máximo para cumplir el margen mínimo $m_{\min}$):
  $$\text{TRM}_{\text{ef}}^* = \frac{P \cdot (1 - c - m_{\min}) - F - O}{K}$$
* **TRM Oficial de Quiebre:**
  $$\text{TRM}^* = \frac{\text{TRM}_{\text{ef}}^*}{1 + \text{sobrecosto}}$$

Donde:
* $P$ = Precio de venta en Mercado Libre (COP).
* $c$ = Comisión porcentual de Mercado Libre (11% a 16%).
* $F$ = Costos fijos por venta en pesos (cargo fijo por venta, costo de envío gratis asumido).
* $O$ = Otros costos en pesos independientes del dólar (empaque, courier local, provisión de riesgo/garantía).
* $K$ = Costo del producto puesto en Colombia expresado **en dólares** (precio compra origen + sales tax + flete internacional en USD + arancel proporcional).
* $\text{TRM}_{\text{ef}}$ = TRM oficial $\times (1 + \text{sobrecosto tarjeta/medio de pago})$.

### Qué se construye:
- `src/costing.py`: Funciones de costo puesto, margen y TRM de quiebre analítica.
- `tests/test_costing.py`: Pruebas automáticas (`pytest`) con casos conocidos.
- `notebooks/02_calibracion_ventas_reales.ipynb`.

### Cómo se hace:
1. Confirmar con fuentes oficiales (DIAN y courier) aranceles e IVA en importaciones pequeñas (< $200 USD / TLC).
2. Cargar en la tabla `orders` tus **3 ventas reales** con todos los costos reales que pagaste.
3. Correr la calculadora sobre esas 3 ventas y comparar margen calculado vs. margen real.
4. Calibrar parámetros en `config.yaml` hasta que la diferencia sea explicable y mínima.
5. Parametrizar la tasa real de sobrecosto de tu tarjeta bancaria.

* **Listo cuando:** La calculadora reproduce el margen real de tus 3 ventas pasadas con una diferencia pequeña y explicable.

---

## 🔹 Fase 4: Lado de costos, emparejamiento y primera Ficha de Oportunidad

* **Objetivo:** Que el sistema te muestre productos concretos para comprar, con su margen y proveedor óptimo.
* **Por qué aquí:** Ya se tiene la demanda (Fase 2) y la calculadora (Fase 3). Falta la oferta y el vínculo entre ambas.

### Qué se construye:
- `src/sources/amazon_watchlist.py`: Revisa precios de una **lista de ASINs** preseleccionada.
- `src/sources/ebay.py`: Consulta la API oficial de eBay (solo producto nuevo).
- `data/watchlist.csv`: Lista de productos vigilados.
- `data/matches.csv` / tabla `product_matches`: Equivalencias **curadas manualmente por Julián**.
- `src/opportunities.py`: Cruza demanda, costo y margen.

### Cómo se hace:
1. Comenzar con **dos proveedores**: Amazon (Watchlist) y eBay (solo nuevo).
2. Para cada producto líder de Mercado Libre (Fase 2), buscar el equivalente en la lista. Emparejar por **número de parte, modelo y capacidad**, aprobado por Julián.
3. Calcular para cada pareja el margen y la TRM de quiebre.
4. Generar la **Ficha de Oportunidad**: producto, link de compra, precio en origen, costo puesto, precio sugerido en Meli, margen neto, TRM de quiebre, competidores y nivel de confianza.

* **Listo cuando:** El sistema produce una lista de al menos 10 fichas para una categoría y tú las revisas y apruebas o descartas.

---

## 🔹 Fase 5: Panel, alertas y reglas del dólar

* **Objetivo:** Que el sistema sirva en el día a día desde el celular y que las reglas del dólar estén respaldadas por datos.

### Qué se construye:
- `app/dashboard.py` en Streamlit: Tabla de oportunidades, botones de aprobar/rechazar, gráficos de TRM y precios.
- `src/telegram_bot.py`: Alertas al celular cuando una oportunidad supera el margen mínimo.
- `src/fx_rules.py`: Reglas del dólar.
- `notebooks/03_backtest_dolar.ipynb`.

### Cómo se hace:
1. Mostrar la distancia entre la TRM actual y la TRM de quiebre (margen de seguridad).
2. Incluir medias móviles de 20 y 50 días como **indicador informativo**, no orden ciega.
3. Realizar backtesting de las reglas del dólar comparadas contra una compra periódica fija.
4. Registrar el histórico de aprobaciones y rechazos de Julián para retroalimentar el sistema.

* **Listo cuando:** Recibes alertas reales en Telegram y puedes sustentar con datos empíricos si una regla del dólar aporta o no rentabilidad.

---

## 🔹 Fase 6: Automatización por partes y ampliación

* **Criterio de entrada:** Solo se inicia si las fases 1 a 5 demostraron alta efectividad y rentabilidad. Se ejecuta de menor a mayor riesgo:

1. Actualización automática de precios de tus publicaciones según costo y TRM del día.
2. Publicación de nuevos productos aprobados por ti vía API de Mercado Libre.
3. Seguimiento de pedidos y avisos de ventas.
4. Apoyo para impresión de etiquetas y despacho.
5. Ampliación: nuevos proveedores (Newegg, AliExpress Choice, Woot), nuevas categorías, emparejamiento automático con PLN, optimización de presupuesto (Problema de la Mochila), productos estrella fuera de tecnología y publicaciones en Facebook Marketplace.
6. **Compra automática: la última.** Con tope diario de capital y autorización previa.

---

## 📌 Supuestos Operativos Validados
* **Condición de producto:** Solo producto nuevo (cero reacondicionados ni usados).
* **Nicho inicial:** Hardware de PC (Memorias RAM primero, luego SSDs y monitores).
* **Proveedores iniciales:** Amazon US y eBay Oficial.
* **Canales:** Mercado Libre como canal central; Facebook Marketplace como tarea manual de apoyo publicitario.
* **Parámetros:** Margen mínimo y comisiones centralizados en `config.yaml`.
