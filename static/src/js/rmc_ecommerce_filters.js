odoo.define('rmc_ecommerce_filters.filters', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.RmcEcommerceFilters = publicWidget.Widget.extend({
    // Ahora el selector principal es toda la tarjeta para controlar ambos contenedores
    selector: '.rmc-unified-search-card', 
    events: {
        'change .rmc_filters_container #category_filter': '_onFilterChange',
        'change .rmc_filters_container #on_sale_filter': '_onFilterChange',
    },

    /**
     * @override
     */
    start: function () {
        const filterCollapseEl = this.el.querySelector('#rmcFilterCollapse');
        const filterToggleButton = this.el.querySelector('#rmc_filter_toggle_btn');

        if (!filterCollapseEl || !filterToggleButton) {
            return this._super.apply(this, arguments);
        }

        // --- Lógica para el botón de filtros ---
        // Cambia el estilo del botón cuando el panel se muestra o se oculta
        const toggleButtonClass = () => {
            if (filterCollapseEl.classList.contains('show')) {
                filterToggleButton.classList.add('active');
            } else {
                filterToggleButton.classList.remove('active');
            }
        };

        // Escuchar eventos de Bootstrap para actualizar el botón
        filterCollapseEl.addEventListener('shown.bs.collapse', toggleButtonClass);
        filterCollapseEl.addEventListener('hidden.bs.collapse', toggleButtonClass);
        
        // Estado inicial
        toggleButtonClass();

        return this._super.apply(this, arguments);
    },

    /**
     * Al cambiar cualquier filtro, se envía el formulario completo.
     */
    _onFilterChange: function (ev) {
        this.el.closest('form').submit();
    },
});

return publicWidget.registry.RmcEcommerceFilters;
});