from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from network.models import Product, Company


# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'network_type', 'provider_link', 'debt', 'city')
    list_filter = ('city',)
    readonly_fields = ('create_time',)
    fieldsets = [
        (None, {'fields': ['level', 'title', 'network_type', 'provider', 'debt']}),
        ('Контактная информация', {'fields': ['email', 'country', 'city', 'street', 'house']}),
        ('Информация',
         {'fields': ('create_time', 'products')})
    ]

    def provider_link(self, obj):
        if obj.provider:
            url = reverse(
                'admin:network_company_change',
                args=(obj.provider.id,)
            )
            return mark_safe(u'<a href="{0}">{1}</a>'.format(url, obj.provider))

    provider_link.short_description = 'Поставщик'

    actions = ['clear_debt']

    @admin.action(description='Очиcтить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)


admin.site.register(Product)
