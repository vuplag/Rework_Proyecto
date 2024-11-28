from django.urls    import path
from Login.views    import Login, Logout_view
from Register.views import Register_view
from MainPG.views   import Home
from Terry.views    import Terry
from Terry.views    import Terry
from Trivia.views   import Trivia
from Skins.views    import Skins
from Tips.views     import Consejos
from Login.views    import Logout_view




urlpatterns = [
    path('Login/',          Login,         name = 'login'       ),
    path('Register/',       Register_view, name = 'register'    ),
    path('Logout/',         Logout_view,   name = 'logout'      ), 
    path('',                Home            ),
    path('Terry/',          Terry,          name = 'home'       ),
    path('Terry/Trivia/',   Trivia          ),
    path('Terry/Skins/',    Skins           ),
    path('Terry/Consejos/', Consejos        ),
]