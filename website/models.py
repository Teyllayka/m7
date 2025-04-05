from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from ckeditor.fields import RichTextField

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        if not password:
            raise ValueError('The password must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True) 
    phone = models.CharField(max_length=20, blank=True, null=True) 

    class Meta:
        verbose_name = "Организации"
        verbose_name_plural = "Организации"

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  

    objects = CustomUserManager()

    def __str__(self):
        return self.username


   
class Pages(models.Model):
    page = models.CharField(max_length=255)
    content = RichTextField()

    class Meta:
        verbose_name = "Страницы"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.page