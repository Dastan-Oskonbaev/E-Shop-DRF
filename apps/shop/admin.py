from django import forms
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category,   Product, Specification


class SpecificationInLine(admin.TabularInline):
    model = Specification
    extra = 1


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
    )
    list_display_links = (
        'indented_title',
    )
    list_filter = ['parent']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "quantity", "description")
    list_filter = ("name", "category", "price", "quantity", "description")
    search_fields = ("name", "category", "price", "quantity", "description")
    inlines = [SpecificationInLine]
    save_on_top = True


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')
    list_filter = ('product',)
    search_fields = ('product__name',)



admin.site.site_title = 'E Shop'
admin.site.site_header = 'E Shop'