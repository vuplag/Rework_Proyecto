from django.urls import path
from . import views

urlpatterns = [
    path('',                                 views.Terry,           name = 'terry_home'   ),
    path('Trivia/',                          views.Trivia,          name = 'Trivia'       ),
    path('Consejos/',                        views.Consejos,        name = 'Consejos'     ),
    path('Skins/',                           views.Skins,           name = 'Skins'        ),
    path('SeleccionarSkin/<str:skin_name>/', views.SeleccionarSkin, name = 'SeleccionarSkin'),
    path('Gameover/',                        views.Gameover,        name = 'Gameover')
]
