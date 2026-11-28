# 🔍 Hallazgos de Auditoría: API de Mercado Libre Colombia (MCO)

**Fecha de ejecución:** 2026-11-27  
**Entorno de prueba:** Python 3.11 / Requests / Conexión directa a `https://api.mercadolibre.com`  
**Objetivo de Fase 1:** Verificar empíricamente qué datos entrega realmente la API de Mercado Libre y cuáles requieren autenticación o están restringidos.

---

## 🚨 Hallazgo Crítico Principal: Bloqueo de PolicyAgent sin Token

Al consultar los endpoints sin cabecera de autenticación (`Authorization: Bearer <TOKEN>`), la infraestructura de seguridad de Mercado Libre (`PolicyAgent`) bloquea sistemáticamente las consultas de búsqueda y detalle de publicaciones:

```json
{
  "status": 403,
  "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",
  "message": "At least one policy returned UNAUTHORIZED.",
  "blocked_by": "PolicyAgent"
}
```

> **Conclusión Clave:** No es posible construir el pipeline de datos de Mercado Libre usando peticiones públicas anónimas. **Es indispensable contar con una aplicación registrada en el portal de desarrolladores de Mercado Libre (`MELI_ACCESS_TOKEN`)**.

---

## 📊 Matriz de Endpoints Auditados

| Endpoint | Parámetros Probados | Status Code Sin Token | Diagnóstico y Comportamiento |
| :--- | :--- | :---: | :--- |
| `/sites/MCO/search` | `q=memoria+ram+ddr4+16gb&limit=5` | **403 Forbidden** | Bloqueado por `PolicyAgent`. Requiere `access_token` en header. |
| `/sites/MCO/categories` | Ninguno | **403 Forbidden** | Bloqueado por `PolicyAgent`. |
| `/categories/MCO1648` | `MCO1648` (Computación) | **200 OK** | **Público.** Retorna árbol de subcategorías y volumen de publicaciones. |
| `/categories/MCO1694` | `MCO1694` (Memorias RAM) | **200 OK** | **Público.** 9.874 publicaciones activas al momento del escaneo. |
| `/sites/MCO/trends/search` | Ninguno | **404 Not Found** | Endpoint deprecated o reubicado en la v2 de tendencias. |
| `/items/{item_id}` | `MCO123456789` | **403 Forbidden** | Bloqueado por `PolicyAgent`. Requiere token para leer detalle individual. |

---

## 📁 Registro de Datos Crudos Guardados (`data/raw/`)

Cumpliendo la **Regla 6** del proyecto (*los datos crudos se guardan antes de limpiarse, con fecha y hora*), las respuestas recibidas quedaron almacenadas en:

* `data/raw/meli_raw_search_ram_20261128T032652Z.json`
* `data/raw/meli_raw_site_categories_20261128T032652Z.json`
* `data/raw/meli_raw_category_computacion_20261128T032653Z.json`
* `data/raw/meli_raw_trends_20261128T032653Z.json`

---

## 🌳 Categorías Mapeadas para Hardware de PC

A través del endpoint público `/categories/{id}`, mapeamos el árbol oficial de categorías para enfocar la Fase 2:

* **Categoría Raíz:** `MCO1648` (Computación - 2.611.024 ítems)
  * `MCO441358` (Componentes de PC - 222.804 ítems)
    * 🎯 **`MCO1694` Memorias RAM** (9.874 ítems) $\rightarrow$ *Nuestra categoría inicial de Fase 2*
    * `MCO430796` Discos y Accesorios / SSDs (15.676 ítems)
    * `MCO1693` Procesadores (4.196 ítems)
    * `MCO430916` Fuentes de Alimentación (31.065 ítems)
    * `MCO455814` Tarjetas de Video / Expansión (44.484 ítems)

---

## 📋 Pasos Pendientes para Julián (Lo que solo tú puedes hacer)

Para completar la Fase 1 y pasar a la Fase 2, se requiere:

1. **Crear la App de Desarrollador en Mercado Libre:**
   * Entrar a [developers.mercadolibre.com.co](https://developers.mercadolibre.com.co) con tu usuario de Mercado Libre.
   * Ir a **Mis aplicaciones** $\rightarrow$ **Crear nueva aplicación**.
   * Nombre sugerido: `meli-arbitrage-analytics`.
   * En Redirect URI poner: `https://localhost/callback`.
   * Habilitar permisos de lectura (*Read*).
2. **Obtener Credenciales:**
   * Copiar `App ID` y `Client Secret`.
   * Generar un `access_token` de prueba.
3. **Guardar en tu archivo `.env` local:**
   ```env
   MELI_APP_ID=tu_app_id
   MELI_SECRET_KEY=tu_secret_key
   MELI_ACCESS_TOKEN=tu_token_aqui
   ```
4. **Verificación final:**
   * Una vez ingresado el token, ejecutaremos una búsqueda autenticada para confirmar si `sold_quantity` viene exacto o por rangos y validar los campos del vendedor.
