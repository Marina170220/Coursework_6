from django.core.validators import MinLengthValidator
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(verbose_name="Название товара", help_text="Введите название товара", max_length=200,
                             validators=[MinLengthValidator(1)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор объявления",
                               help_text="Укажите автора объявления")
    price = models.PositiveIntegerField(verbose_name="Цена товара", help_text="Добавьте цену товара")
    description = models.TextField(verbose_name="Описание товара", help_text="Введите описание товара", max_length=1000)
    created_at = models.DateTimeField(verbose_name="Дата и время создания объявления", auto_now_add=True)
    image = models.ImageField(verbose_name="Фото", help_text="Разместите фото для объявления", null=True, blank=True,
                              upload_to="images/")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(verbose_name="Комментарий", help_text="Оставьте свой комментарий здесь", max_length=1000,
                            validators=[MinLengthValidator(1)])
    author = models.ForeignKey(User, verbose_name="Автор комментария", related_name="comments", on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, verbose_name="Объявление", related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Дата и время создания комментария", auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
