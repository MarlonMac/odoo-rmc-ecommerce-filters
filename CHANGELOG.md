# Historial de Cambios

## [16.0.2.0] - 2025-07-31

### ✨ Características
* **Filtro de Subcategorías Dinámico:** Se implementa un sistema de filtrado por categorías y subcategorías robusto basado en la navegación por URL nativa de Odoo, mejorando la estabilidad y la experiencia de usuario.
* **Filtro por Rango de Precios:** Se integra exitosamente el slider de precios nativo de Odoo, garantizando un rendimiento óptimo y una experiencia visual profesional.

### 🐛 Correcciones y Mejoras
* **Integración Visual:** Se han desarrollado estilos CSS a medida para que el slider de precios nativo se integre perfectamente con el diseño minimalista del módulo.
* **Rendimiento del Backend:** Se ha optimizado el controlador para calcular los rangos de precios de forma eficiente, evitando la ralentización en catálogos con muchos productos.
* **Estabilidad General:** Se refactorizó el código de JavaScript y del controlador para eliminar errores, mejorar la legibilidad y asegurar un comportamiento predecible de todos los filtros.

## [16.0.1.5] - 2025-07-31

### ✨ Características
* **Filtro de Subcategorías Funcional:** El filtro de subcategorías ahora funciona de forma nativa, redirigiendo a la URL de la subcategoría seleccionada para un filtrado preciso y estable.

### 🐛 Correcciones y Mejoras
* **Estabilidad del Controlador:** Se ha refactorizado por completo el controlador principal para eliminar los errores "Internal Server Error" y seguir las mejores prácticas de Odoo.
* **Lógica de Filtros Activos:** Se ha corregido el indicador visual "Filtros" para que se active correctamente cuando se selecciona una categoría o se aplica un filtro de ofertas.

## [16.0.1.0.3] - 2025-07-06

### ✨ Características
* **Diseño de Filtros Colapsable:** Se añade un botón "Filtros" que muestra/oculta el panel de filtros con una animación suave, manteniendo la interfaz limpia por defecto.
* **Estilo de Interruptor Personalizado:** Se reemplaza el *checkbox* de "Ofertas" por un interruptor de palanca (`toggle switch`) moderno y estilizado para una mejor experiencia visual.
* **Tema de Diseño Claro:** Se implementa un tema con fondo blanco y controles oscuros para una apariencia más moderna y profesional.
* **Aplicación Automática de Filtro de Ofertas:** Al igual que el filtro de categoría, el interruptor de "Ofertas" ahora aplica el filtro automáticamente sin necesidad de un botón "Aplicar".

### 🐛 Correcciones y Mejoras
* **Soporte Multi-Sitio Web:** Se ajusta la definición de la vista para asegurar que el bloque de filtros se aplique correctamente en todas las instancias de sitios web de Odoo.
* **Unificación de Estilos:** Se ajustan los estilos de los menús desplegables y botones para que sean visualmente consistentes en todo el bloque de filtros.
* **Ajuste de Diseño Visual:** Se elimina el espacio superior entre la barra de navegación y el bloque de filtros, y se ajustan los bordes para una integración perfecta.

## [16.0.1.0.2] - Fecha Inicial

### ✨ Características
* **Creación del Módulo Base:** Se crea la estructura inicial del módulo.
* **Bloque de Filtros Unificado:** Se reemplaza el `header` de la tienda por una tarjeta unificada que contiene la búsqueda y placeholders para filtros.
* **Filtro "En Oferta":** Se añade la lógica del controlador y el modelo para permitir filtrar productos marcados como `is_on_sale`.
* **Filtro por Categoría:** Se implementa la funcionalidad para que el filtro por categoría se aplique automáticamente al seleccionar una opción.

### 🐛 Correcciones
* **Búsqueda Funcional:** Se corrige el error inicial que impedía el funcionamiento de la barra de búsqueda al moverla a un nuevo contenedor.