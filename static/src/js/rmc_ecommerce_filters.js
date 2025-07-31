odoo.define('rmc_ecommerce_filters.filters', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.RmcEcommerceFilters = publicWidget.Widget.extend({
    selector: '.rmc-unified-search-card', 
    events: {
        'change #category_filter': '_onCategoryChange',
        'change #subcategory_filter': '_onSubcategoryChange',
        'change #on_sale_filter': '_onSaleFilterChange',
    },

    start: function () {
        const parentCategoryId = this.$el.closest('form').data('selected-parent-id');
        if (parentCategoryId) {
            this._updateSubcategories(parentCategoryId);
        }
        return this._super.apply(this, arguments);
    },

    _onCategoryChange: function (ev) {
        const $target = $(ev.currentTarget);
        const categoryId = $target.val();
        
        if (categoryId) {
            this._rpc({
                route: '/shop/subcategories',
                params: { category_id: categoryId },
            }).then(subcategories => {
                if (subcategories && subcategories.length > 0) {
                    this._updateSubcategories(categoryId);
                } else {
                    const categorySlug = $target.find('option:selected').data('slug');
                    window.location.href = '/shop/category/' + categorySlug;
                }
            });
        } else {
            window.location.href = '/shop';
        }
    },

    _onSubcategoryChange: function(ev) {
        const $target = $(ev.currentTarget);
        const subcategorySlug = $target.find('option:selected').data('slug');
        if (subcategorySlug) {
            window.location.href = '/shop/category/' + subcategorySlug;
        }
    },

    _onSaleFilterChange: function() {
        this.el.closest('form').submit();
    },

    _updateSubcategories: function (categoryId) {
        const $subCategorySelect = this.$('#subcategory_filter');
        const selectedSubId = this.$el.closest('form').data('selected-subcategory-id');

        this._rpc({
            route: '/shop/subcategories',
            params: { category_id: categoryId },
        }).then(function (subcategories) {
            $subCategorySelect.find('option:not(:first)').remove();

            if (subcategories && subcategories.length > 0) {
                $subCategorySelect.prop('disabled', false);
                subcategories.forEach(function (sub) {
                    const option = new Option(sub.name, sub.id);
                    $(option).data('slug', sub.slug);
                    if (sub.id === selectedSubId) {
                        $(option).prop('selected', true);
                    }
                    $subCategorySelect.append(option);
                });
            } else {
                $subCategorySelect.prop('disabled', true);
            }
        });
    },
});

return publicWidget.registry.RmcEcommerceFilters;
});