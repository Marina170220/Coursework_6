from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles:
    ADMIN = 'admin'
    USER = 'user'
    roles = ((ADMIN, ADMIN), (USER, USER))


class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name="Имя", help_text="Введите имя, макс 64 символа", max_length=64)
    last_name = models.CharField(verbose_name="Фамилия", help_text="Введите фамилию, макс 64 символа", max_length=64)
    phone = models.CharField(verbose_name="Телефон для связи", help_text="Укажите телефон для связи", max_length=128)
    email = models.EmailField(verbose_name="Email address", help_text="Укажите электронную почту", unique=True,
                              max_length=254)
    role = models.CharField(choices=UserRoles.roles, default=UserRoles.USER, max_length=5)
    is_active = models.BooleanField(default=True, verbose_name="Аккаунт активен",
                                    help_text="Укажите, активен ли аккаунт")
    image = models.ImageField(verbose_name="Аватарка", help_text="Разместите Вашу фотографию", null=True, blank=True,
                              upload_to="photos/")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
