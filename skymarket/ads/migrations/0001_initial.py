# Generated by Django 3.2.6 on 2022-06-17 17:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название товара', max_length=200, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Название товара')),
                ('price', models.PositiveIntegerField(help_text='Добавьте цену товара', verbose_name='Цена товара')),
                ('description', models.TextField(help_text='Введите описание товара', max_length=1000, verbose_name='Описание товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания объявления')),
                ('image', models.ImageField(blank=True, help_text='Разместите фото для объявления', null=True, upload_to='images/', verbose_name='Фото')),
                ('author', models.ForeignKey(help_text='Укажите автора объявления', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор объявления')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Оставьте свой комментарий здесь', max_length=1000, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания комментария')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ads.ad', verbose_name='Объявление')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
