from django.db import models


class OrderHeaders(models.Model):
    reg_number = models.CharField(verbose_name="Регистрационный номер заказа", max_length=100, unique=True)
    on_date = models.DateTimeField(verbose_name="Дата формирования заказа", auto_now_add=True)
    is_active = models.BooleanField(db_index=True, verbose_name="Заказ активен", default=True)

    def __str__(self):
        return self.reg_number


class OrderDetails(models.Model):
    hdr = models.ForeignKey(OrderHeaders, verbose_name="Идентификатор товара", on_delete=models.CASCADE)
    good_id = models.DecimalField(verbose_name="Идентификатор товара", max_digits=10, decimal_places=0)
    amount = models.DecimalField(verbose_name="Количество товара", max_digits=19, decimal_places=4, default=0)
    price = models.DecimalField(verbose_name="Цена за единицу измерения товара для данного заказа",
                                max_digits=19, decimal_places=2, default=0)
    is_active = models.BooleanField(db_index=True, verbose_name="Деталь заказа активна", default=True)

    def product_cost(self):
        "return cost of all products this type"
        return self.amount * self.price

