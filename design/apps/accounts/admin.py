from django.contrib import admin
from .models import Profile
from django.contrib.auth.forms import AdminPasswordChangeForm
from ..services.models import ServiceSet
from django.urls import reverse
from django.utils.safestring import mark_safe


class ServiceSetInline(admin.TabularInline):
    model = ServiceSet
    extra = 0
    fields = ['link_to_service_set', 'is_active', 'total_price', 'items_cnt']  # Поля, отображаемые в одной строке
    readonly_fields = ['link_to_service_set', 'total_price', 'items_cnt']  # Делаем ссылку только для чтения

    def link_to_service_set(self, instance):
        url = reverse('admin:%s_%s_change' % (instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        return mark_safe('<a href="%s">%s</a>' % (url, "Перейти к заказу"))

    link_to_service_set.short_description = "Заказ"

    def total_price(self, instance):
        return instance.total_price

    def items_cnt(self, instance):
        return instance.items_cnt

    total_price.short_description = "Общая стоимость"
    items_cnt.short_description = "Количество услуг"


class IsDesignerFilter(admin.SimpleListFilter):
    title = 'Является дизайнером'
    parameter_name = 'is_designer'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Да'),
            ('no', 'Нет'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(is_designer=True)
        if self.value() == 'no':
            return queryset.filter(is_designer=False)


class ProfileAdmin(admin.ModelAdmin):
    change_password_form = AdminPasswordChangeForm
    list_filter = (IsDesignerFilter, )
    inlines = [ServiceSetInline]
    search_fields = ["last_name", "first_name", "patronymic", "email", "phone_number"]
    fieldsets = (
            (None, {"fields": ("username", "password")}),
            (("Персональные данные"), {"fields": ("last_name", "first_name", "patronymic")}),
            (   ("Контактные данные"), {"fields": ("email", "phone_number")}),
            (   ("Даты"), {"fields": ("last_login", "date_joined")}),
            (
                ("Права"),
                {
                    "fields": (
                        "is_designer",
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            
        )
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("username", "usable_password", "password1", "password2"),
                },
            ),
        )


admin.site.register(Profile, ProfileAdmin)
