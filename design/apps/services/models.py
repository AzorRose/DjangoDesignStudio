from django.db import models
from ..accounts.models import Profile


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Мин. стоимость")
    spec_types = [("Веб-дизайн", "Веб-дизайн"),
                  ("Графический дизайн", "Графический дизайн"),
                  ("Дизайн интерьера", "Дизайн интерьера")]
    specialization = models.CharField(choices=spec_types, max_length=50, verbose_name="Специализация")
    
    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f"{self.name}"

class ServiceSet(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, db_index=True, related_name="service_set", verbose_name="Заказчик")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    @property
    def total_price(self):
        # Используйте агрегацию для суммирования цен SetItem
        return sum(item.price for item in self.items.all())

    @property
    def items_cnt(self):
        # Просто используйте метод count для подсчета элементов
        return self.items.count()

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.id}"
        

class SetItem(models.Model):
    serviceset = models.ForeignKey(ServiceSet, related_name='items', on_delete=models.CASCADE, verbose_name="Заказ")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    volume = models.PositiveIntegerField(default=1, verbose_name="Объем")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    
    class Meta:
        verbose_name = "Заказанные услуги"
        verbose_name_plural = "Заказанные услуги"