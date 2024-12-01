from django.urls       import path, include
from Login.views       import Login, Logout_view
from Register.views    import Register_view
from MainPG.views      import Home
from Terry.views       import Terry
from Terry             import urls
from Login.views       import Logout_view
from django.contrib    import admin
from Vidas_Terry.views import menu_principal


urlpatterns = [
    path('Login/',          Login,         name = 'login'       ),
    path('Register/',       Register_view, name = 'register'    ),
    path('Logout/',         Logout_view,   name = 'logout'      ), 
    path('',                Home                                ),
    path('Terry/',          include('Terry.urls')               ),
    path('admin/',          admin.site.urls                     ),
    path('mascota/<int:mascota_id>/', menu_principal, name='menu_principal'),
]