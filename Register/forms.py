from django import forms
from .models import Usuarios

class RegistroForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña'}),
        label="Contraseña",
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}),
        label="Confirmar contraseña",
    )

    class Meta:
        model = Usuarios
        fields  = ['nombre', 'mail']
        widgets = { 
            'nombre': forms.TextInput (attrs={'placeholder': 'Ingresa tu nombre'}),
            'mail'  : forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
