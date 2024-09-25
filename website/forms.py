from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from website.models import CustomUser
from datetime import datetime


class PasswordOnlyAuthenticationForm(forms.Form):
    password = forms.CharField(
        strip=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите ваш пароль",
            }
        ),
        error_messages={
            "required": "Поле пароля не может быть пустым.",
        },
    )

    def clean(self):
        password = self.cleaned_data.get("password")

        user = None
        for candidate_user in CustomUser.objects.all():
            if candidate_user.check_password(password):
                user = candidate_user
                break
        if user is None:
            raise ValidationError("Неверный пароль.")
        return {"user": user}


class CarPassForm(forms.Form):
    today = datetime.today()
    formatted_date = today.strftime("%Y-%m-%d")

    CAR_TYPE_CHOICES = [
        ("8", "Легковой"),
        ("10", "Грузовой"),
    ]

    car_number = forms.CharField(
        label="Номер автомобиля",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Номер автомобиля"}
        ),
    )

    car_type = forms.ChoiceField(
        label="Выберите тип автомобиля",
        choices=CAR_TYPE_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
    )

    entry_date = forms.DateField(
        label="Дата заезда",
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "id": "date",
                "placeholder": "Дата заезда",
                "type": "date",
                "min": formatted_date,
            }
        ),
    )


class SupportRequestForm(forms.Form):
    contact_name = forms.CharField(
        label="Контактное лицо",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Контактное лицо"}
        ),
    )
    phone_number = forms.CharField(
        label="Телефон",
        max_length=18,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "+7 (999) 999-99-99",
                "autocomplete": "off",
            }
        ),
    )
    message = forms.CharField(
        label="Текст обращения",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Текст обращения"}
        ),
    )
