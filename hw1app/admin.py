from django.contrib import admin
from hw1app.models import Client, Goods, Order

@admin.action(description = "Обновняем описание")
def update_description(modeladmin, request, queryset):
    queryset.update(description='Описание обновлено')


@admin.action(description = "Обнуление цены")
def reset_price(modeladmin, request, queryset):
    queryset.update(price=0)


@admin.action(description="Премиум")
def filter_price(modeladmin, request, queryset):
    queryset.filter(price__gt=10).update(description="Премиум")


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'quantity', 'date_of_add']
    ordering = ['title', '-price']
    list_per_page = 5
    search_fields = ['title']
    actions = [reset_price, update_description, filter_price]
    fieldsets = [
        (
            'Наименование товаров',
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Описание товара',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['description'],
        },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Дата регистрации товара',
            {
                'fields': ['date_of_add'],
            }
        ),
    ]




admin.site.register(Client)
#admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order)


