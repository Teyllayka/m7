from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

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

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ПВР и ППБ"
        verbose_name_plural = "ПВР и ППБ"

    def __str__(self):
        return self.title


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Организации"
        verbose_name_plural = "Организации"

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # No required fields other than username

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    published_at = models.DateField(null=True, blank=True)  # Allows date selection only

    class Meta:
        verbose_name = "Календарь мероприятий"
        verbose_name_plural = "Календарь мероприятий"

   

class Phone(models.Model):
    phone = models.CharField(max_length=255)
    phone_displayed = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефон"

    def __str__(self):
        return self.phone


class Pages(models.Model):
    page= models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Страницы"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title