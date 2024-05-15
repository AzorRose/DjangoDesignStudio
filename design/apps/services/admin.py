from django.contrib import admin
from .models import Service, ServiceSet, SetItem

# Register your models here.
class SetItemTabular(admin.TabularInline):
    model = SetItem
    extra = 0


class IsActiveFilter(admin.SimpleListFilter):
    title = 'Активен'
    parameter_name = 'is_active'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Да'),
            ('no', 'Нет'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(is_active=True)
        if self.value() == 'no':
            return queryset.filter(is_active=False)

class ServiceSetAdmin(admin.ModelAdmin):
    inlines = [SetItemTabular]
    list_filter = (IsActiveFilter, )


class ServiceSpecFilter(admin.SimpleListFilter):
    title = 'Специализация'
    parameter_name = 'specialization'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Веб-дизайн'),
            ('2', 'Графический дизайн'),
            ('3', 'Дизайн интерьера')
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(specialization='Веб-дизайн')
        if self.value() == '2':
            return queryset.filter(specialization='Графический дизайн')
        if self.value() == '3':
            return queryset.filter(specialization='Дизайн интерьера')


class ServiceAdmin(admin.ModelAdmin):
    list_filter = (ServiceSpecFilter, )
    search_fields = ["name", ]

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceSet, ServiceSetAdmin)