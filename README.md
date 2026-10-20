# Antonio Colyn · Sitio one-page

Sitio estático ligero para Vercel. Contiene exactamente cinco secciones (#inicio, #ayuda, #servicios, #antonio, #ubicacion), identidad gráfica vectorial y favicon, diseño responsive, navegación accesible y atribución a RAUVIA Consulting.

## Estado de información

**Datos de ubicación y contacto aportados por el cliente (2026-10-20):** Progreso 13, Santa María Tomatlán, Iztapalapa, 09870 Ciudad de México, CDMX; WhatsApp +52 55 7414 0935. El iframe usa la dirección completa como consulta geográfica (no una búsqueda por categoría). El CTA usa https://wa.me/525574140935 con un mensaje prellenado. **Validación pendiente:** comprobar visualmente el pin resultante en Google Maps y probar el enlace en un teléfono con WhatsApp. Horarios, servicios individualizados y credenciales todavía no están confirmados. No afirmar tratamientos o resultados clínicos sin respaldo.

## Antes de publicar

1. Comprobar en móvil que el botón de WhatsApp abre al destinatario +52 55 7414 0935 y verificar la conformidad del profesional con su publicación. El vínculo funciona sin JavaScript.
2. Verificar en Google Maps que la consulta de dirección completa apunta exactamente a Progreso 13, Santa María Tomatlán, Iztapalapa, 09870 CDMX. Si el resultado geocodificado no corresponde al inmueble, sustituirlo por la inserción oficial del pin de negocio.
3. Confirmar títulos, cédula(s), formación, servicios, horarios, perfil de pacientes y fotografía propia autorizada; reemplazar el texto temporal en #antonio y ampliar servicios solo con los confirmados.
4. Revisar el SEO implementado y ejecutar `python3 tests/seo_audit.py`; los metadatos y Schema.org están publicados con los datos aportados. No agregar estrellas, reseñas, horarios ni credenciales sin fuente.
5. Verificar en iPhone, Android y escritorio. Lighthouse accesibilidad, rendimiento y SEO. Confirmar políticas de privacidad si más adelante se instrumentan analíticas o formularios.

## Descubrimiento y posicionamiento

El motor SEO + GEO generativo + LLMO incluye URL canónica única, JSON-LD de 6 nodos relacionados, robots.txt, sitemap.xml, llms.txt y respuestas visibles sobre ubicación/citas/áreas profesionales. La capa de búsqueda local enfatiza Santa María Tomatlán e Iztapalapa sin páginas duplicadas por colonia. Consultar `SEO-GEO-LLMO.md` para criterios, medidas de operación, alta de la web en el Perfil de Empresa de Google y pasos de Search Console/Bing. La auditoría de GitHub Actions verifica coherencia del NAP y de los archivos de descubrimiento.

## Rendimiento móvil (octubre 2026)

- HTML + CSS + JavaScript nativo: no framework ni dependencias de ejecución.
- En pantallas de hasta 760px se emplean fuentes del sistema. El CSS de Google Fonts se solicita únicamente en escritorio para conservar allí el estilo editorial; también se retiraron las conexiones anticipadas a Google Fonts.
- El mapa mantiene el domicilio y enlace a indicaciones disponibles desde el primer render. El iframe de Google Maps no tiene `src` inicial y se solicita al llegar cerca del mapa mediante IntersectionObserver, o al tocar «Mostrar mapa interactivo». Si JavaScript está deshabilitado o falla el mapa, el enlace externo de indicaciones permanece disponible.
- El mismo SVG local se reutiliza en encabezado, hero y footer, aprovechando caché sin duplicar archivos de imagen.
- El CTA directo de WhatsApp sigue operando con HTML, sin esperar a JavaScript.
- Se actualizaron las pruebas de regresión para impedir descargas anticipadas del mapa, fuentes externas en móvil o pérdida de datos SEO.

**Verificación de campo pendiente:** medir Lighthouse/PageSpeed Insights en modo móvil y Core Web Vitals reales (LCP, INP, CLS) cuando haya acceso de red/herramienta a la URL de producción. No se deben inventar puntuaciones o porcentajes de mejora sin una comparación reproducible. Probar también menú móvil, mapa y WhatsApp sobre un teléfono.

## Despliegue

Importar este repositorio en Vercel y usar preset **Other**, Framework: No framework, Build command vacío, Output directory raíz. Todo es estático, no hace falta npm ni variables de entorno.

## Método

Diseño apoyado en AETHRYON OS DRAFT v2.0.0 (18-10-2026): diferenciación hecho/inferencia/hipótesis, desconocidos como null, no presentar métricas inventadas. Con dirección aportada por el usuario existe una base de SEO local; el pin exacto sigue pendiente de comprobación cartográfica. No se asignan puntuaciones CIV/Convergencia/Tyche ni mejoras de ranking sin medición.
