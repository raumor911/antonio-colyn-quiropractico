# Motor SEO, GEO local y LLMO — Antonio Colyn

**Versión inicial:** 2026-10-19. **URL canónica:** https://antonio-colyn-quiropractico.vercel.app/

## Diseño: mínima complejidad y alta coherencia

Solo hay una página comercial indexable. Su estructura conserva cinco secciones. **GEO** aquí significa posicionamiento geográfico/local (no una técnica especial de ranking). **LLMO** significa que los hechos públicos son legibles, verificables y consistentes para sistemas de recuperación e IA. No se simulan rich results ni se promete aparición en resúmenes de IA.

### Contrato de identidad (único negocio, un domicilio)

- Nombre visible: Antonio Colyn; marca mostrada: Antonio Colyn | Fisioterapia y Quiropráctica.
- Dirección facilitada por el cliente: Progreso 13, Santa María Tomatlán, Iztapalapa, C. P. 09870, Ciudad de México, CDMX.
- WhatsApp: +52 55 7414 0935. URL sin trackers: https://wa.me/525574140935.
- Áreas publicadas: fisioterapia y quiropráctica. No confirmar técnicas ni tratamientos más específicos sin su validación.
- Horarios, cédulas, trayectoria, reseñas y coordenadas: desconocidos (no publicar ni simular).

### Descubrimiento e identidad

| Componente | Archivo | Función |
| --- | --- | --- |
| Página semántica | index.html | H1, title, description, copy geográfico natural, respuestas visibles y NAP |
| URL canónica | index.html | Consolidar señales en https://antonio-colyn-quiropractico.vercel.app/ |
| JSON-LD | index.html | WebSite, WebPage, ProfessionalService, Person, Service enlazados por @id |
| Descubrimiento | robots.txt, sitemap.xml | Habilitar rastreo y exponer únicamente la canónica |
| LLMO experimental | llms.txt | Respuestas breves sobre identidad, ubicación, canales y límites |
| QA SEO | tests/seo_audit.py | Comprobar cinco secciones y consistencia de URL, contacto y dirección |

El directorio `/assets` incluye el logo aprobado. La dirección debe validarse en el pin de Google Maps antes de afirmar exactitud cartográfica. Evitar latitud/longitud estimadas.

### Google Search Console

1. Reclamar la propiedad de la URL de producción; verificar por el método que acepte el titular. No almacenar tokens de verificación en código sin razón.
2. Enviar `https://antonio-colyn-quiropractico.vercel.app/sitemap.xml` y solicitar inspección de `https://antonio-colyn-quiropractico.vercel.app/`.
3. Revisar indexación, selección de canónica, búsquedas que generan impresiones, clics y CTR; no asumir que publicar es estar indexado.
4. **Con autorización de Antonio:** añadir `https://antonio-colyn-quiropractico.vercel.app/` en su Perfil de Empresa de Google; igualar nombre, dirección y teléfono a la información real de su ficha. No editar ficha ajena sin autorización.
5. Confirmar categoría principal, servicios, fotos y horarios reales en GBP. Evitar nombres con términos SEO agregados si no forman parte del nombre comercial real.

### Bing Webmaster Tools

Verificar propiedad, enviar sitemap y monitorizar cobertura. IndexNow es optativo: solo habilitar si existe clave válida publicada y se ha probado el protocolo. Para una sola página con cambios esporádicos, no instalar automatizaciones innecesarias.

### Protocolo AETHRYON

- Hechos: ubicación y contacto aportados por el cliente; dos áreas publicadas.
- Inferencia: búsquedas por colonia + servicio expresan una intención local relevante.
- Incertidumbre: mapa/Place ID, credenciales, horarios, reviews, actividad de Search Console y evolución real del posicionamiento.
- Convergencia/CIV/Tyche: hipótesis estratégicas, **sin cifras ni probabilidades** por falta de calibración y métricas de resultado.
- NOX: no asignar score sin los cinco factores evaluados con evidencia. Información del consultorio aún incompleta.

### Medición mensual ligera

Registrar: URL indexada sí/no; impresiones, clics, CTR y consultas con intención local en Search Console; clics en web y solicitud de indicaciones del Perfil de Empresa (si disponibles); conversaciones originadas en la página (medición consentida sin capturar contenido clínico). Revisar NAP entre web, GBP y cualquier perfil controlado. No atribuir causalidad a LLMO sin comparación/control.

### Fuentes metodológicas

- https://developers.google.com/search/docs/appearance/structured-data/local-business
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://www.bing.com/webmasters/help/bing-webmaster-guidelines-30fba23a

### No introducir

Landing pages por colonia sin valor distinto; FAQPage para forzar resultados enriquecidos; reviews, estrellas o testimonios inventados; geo-coordenadas inferidas; títulos o credenciales no confirmados; `meta keywords`; repetición excesiva de keywords; bloqueo de rastreadores en robots.txt; IndexNow sin clave verificada; datos personales clínicos en analítica.
