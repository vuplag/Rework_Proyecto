from django.shortcuts import render, get_object_or_404
from Vidas.models import Mascota

def menu_principal(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)

    # Actualiza el estado de la mascota antes de mostrar el menú
def actualizar_estado_mascota(request, mascota):

    if mascota.estado == 'gameover':
        return render(request, 'gameover.html', {'mascota': mascota})
    elif mascota.estado == 'dañado':
        return render(request, 'menu_dañado.html', {'mascota': mascota})
    else:
        return render(request, 'menu_normal.html', {'mascota': mascota})
