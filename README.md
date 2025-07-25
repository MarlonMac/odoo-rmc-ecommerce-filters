# Módulo de Filtros eCommerce para Odoo 16

## Resumen

Este módulo añade un bloque de filtros avanzado, personalizable y minimalista a la página de la tienda (`/shop`) de Odoo 16, mejorando significativamente la experiencia de usuario.

## Descripción General

El módulo reemplaza la cabecera de búsqueda estándar de la tienda por una "tarjeta" de filtros unificada que se integra visualmente debajo de la barra de navegación principal. Esta tarjeta contiene no solo la barra de búsqueda, sino también los controles de ordenamiento, las opciones de vista (cuadrícula/lista) y un panel de filtros personalizables que se puede mostrar u ocultar con una animación suave.

La funcionalidad está diseñada para ser compatible con entornos multi-sitio web y permite filtrar productos por categoría, subcategoría (placeholder), rango de precios (placeholder) y un filtro especial de "Ofertas".

## Características Principales

* **Bloque de Filtros Unificado:** Integra la búsqueda, el ordenamiento y los filtros en una única tarjeta de diseño limpio.
* **Panel de Filtros Colapsable:** Los filtros detallados (categoría, ofertas, etc.) están ocultos por defecto y se muestran con una animación suave al hacer clic en un botón "Filtros", manteniendo la interfaz despejada.
* **Filtro "En Oferta":**
    * Añade un campo booleano `is_on_sale` al modelo del producto.
    * Proporciona un *toggle switch* de diseño personalizado en el frontend para filtrar productos marcados como oferta.
* **Aplicación de Filtros Automática:** Al cambiar el valor del filtro de categoría o del interruptor de ofertas, la página se actualiza automáticamente sin necesidad de un botón "Aplicar".
* **Diseño Personalizable (CSS):** Incluye un tema "invertido" (fondo claro) y estilos personalizados para todos los elementos, logrando una apariencia simétrica y profesional.
* **Soporte Multi-Sitio Web:** La vista principal está configurada para funcionar correctamente en todos los sitios web de una instancia de Odoo.

## Instalación

1.  Copia la carpeta `rmc_ecommerce_filters` a tu directorio de `addons` de Odoo.
2.  Reinicia el servicio de Odoo.
3.  Ve a **Aplicaciones** en el menú de Odoo.
4.  Haz clic en **Actualizar lista de aplicaciones**.
5.  Busca "Red Music Corporation - eCommerce Filters" y haz clic en **Instalar**.

## Uso y Configuración

### Marcar un Producto como "En Oferta"

1.  Ve al módulo de **Inventario** o **Ventas**.
2.  Selecciona **Productos** > **Productos**.
3.  Abre el producto que deseas marcar como oferta.
4.  En la pestaña **General Information**, busca la opción **"En Oferta"** y activa la casilla.
5.  Guarda los cambios.

### Usar los Filtros en la Tienda

1.  Navega a la página `/shop` de tu sitio web.
2.  El nuevo bloque de filtros aparecerá debajo de la barra de navegación principal.
3.  Usa la barra de búsqueda como lo harías normalmente.
4.  Haz clic en el botón "Filtros" para desplegar las opciones adicionales.
5.  Selecciona una categoría o activa el interruptor "Ofertas". La página se actualizará automáticamente para reflejar tu selección.

## Dependencias

Este módulo depende de los siguientes módulos estándar de Odoo:
* `product`
* `website`
* `website_sale`
* `product_brand_sale`


## Autor

* **Marlon Macario para Red Music Corporation**
* Website: `https://www.link-gt.com`