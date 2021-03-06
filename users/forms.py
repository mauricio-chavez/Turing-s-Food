"""Users app forms"""

from django import forms
from django.contrib.auth import get_user_model

from menu.models import ShoppingCart

User = get_user_model()


class SignupForm(forms.Form):
    """Form for sign up"""
    email = forms.EmailField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    password = forms.CharField(
        min_length=5,
        max_length=128,
        required=True
    )
    password_confirmation = forms.CharField(
        min_length=5,
        max_length=128,
        required=True
    )

    def clean_email(self):
        """Username must be unique."""
        email = self.cleaned_data.get('email')
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError(
                f'{ email } ya está registrado. '
                'Intenta con otro correo.'
            )
        return email

    def clean(self):
        """Passwords must match"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError('Las contraseñas no coinciden.')
        else:
            raise forms.ValidationError('Debes ingresar una contraseña.')

        return cleaned_data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_active=False)
        ShoppingCart.objects.create(user=user)

        return user
