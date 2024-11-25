from django import forms
from .models import Usuarios

class RegistroForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmar contraseña"
    )

    class Meta:
        model = Usuarios
        fields = ['nombre', 'contraseña', 'mail']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("contraseña")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
