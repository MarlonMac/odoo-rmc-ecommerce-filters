# Hoja de Ruta del Proyecto (Roadmap)

Este documento describe las características y mejoras futuras planificadas para el módulo de filtros de eCommerce.

## Próxima Versión (v16.0.2.0)

* **Filtro de Subcategorías Dinámico:**
    * **Objetivo:** Activar el menú desplegable de "Subcategoría".
    * **Comportamiento:** Al seleccionar una categoría principal, el desplegable de subcategorías se cargará automáticamente (vía AJAX) con las subcategorías correspondientes, permitiendo un filtrado más granular.

* **Filtro por Rango de Precios:**
    * **Objetivo:** Implementar un *slider* de rango de precios funcional.
    * **Comportamiento:** Permitir al usuario seleccionar un rango de precios mínimo y máximo para filtrar los productos. El *slider* deberá actualizar los resultados de forma dinámica.

* **Filtro por Marca:**
    * **Objetivo:** Añadir un filtro para seleccionar una o varias marcas de productos.
    * **Comportamiento:** El filtro se basará en el campo del módulo `product_brand_sale`. Podría ser un menú desplegable con *checkboxes* para selección múltiple.

* **Guardar Estado de los Filtros:**
    * **Objetivo:** Recordar los filtros seleccionados por el usuario.
    * **Comportamiento:** Si un usuario abre o cierra el panel de filtros, el estado (abierto/cerrado) y los filtros activos (categoría, ofertas, etc.) se mantendrán durante su sesión de navegación.

## Futuras Mejoras (Post-v16.0.2.0)

* **Sugerencias de Búsqueda (Autocomplete):**
    * **Objetivo:** Restaurar la funcionalidad de autocompletado en la barra de búsqueda que muestra sugerencias de productos mientras el usuario escribe.

* **Indicador de Filtros Activos:**
    * **Objetivo:** Mostrar un pequeño indicador numérico o visual en el botón "Filtros" cuando hay uno o más filtros aplicados, para que el usuario sepa que la vista está filtrada incluso con el panel cerrado.

* **Optimización de Rendimiento:**
    * **Objetivo:** Analizar y optimizar las consultas a la base de datos, especialmente para tiendas con un gran número de productos y atributos, para asegurar que los filtros se apliquen de forma rápida.

* **Más Opciones de Personalización:**
    * **Objetivo:** Permitir a los administradores configurar fácilmente qué filtros están disponibles desde el *backend* de Odoo, sin necesidad de modificar el código.
