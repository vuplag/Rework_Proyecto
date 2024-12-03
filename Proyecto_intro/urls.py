from django.urls       import path, include
from Login.views       import Login, Logout_view, reset
from Register.views    import Register_view
from MainPG.views      import Home
from Terry             import urls
from Login.views       import Logout_view
from django.contrib    import admin



urlpatterns = [
    path('Login/',          Login,         name = 'login'       ),
    path('Register/',       Register_view, name = 'register'    ),
    path('Logout/',         Logout_view,   name = 'logout'      ), 
    path('',                Home                                ),
    path('Terry/',          include('Terry.urls')               ),
    path('admin/',          admin.site.urls                     ),
    path('reset/',          reset,         name = 'reset'       ),
]