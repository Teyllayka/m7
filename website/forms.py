from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from website.models import CustomUser  

class PasswordOnlyAuthenticationForm(forms.Form):
    password = forms.CharField(
        
        strip=False,
        widget=forms.TextInput(attrs={
            'placeholder': "Введите ваш пароль",
        }),
    )

    def clean(self):
        password = self.cleaned_data.get("password")

        user = None
        for candidate_user in CustomUser.objects.all():
            if candidate_user.check_password(password):
                user = candidate_user
                break

        if user is None:
            raise ValidationError("Invalid password.")
        return {'user': user}
