from django.urls    import path
from Login.views    import Login
from Register.views import Register
from MainPG.views   import Home
from Terry.views    import Terry
from Trivia.views   import Trivia
from Skins.views    import Skins
from Tips.views     import Consejos



urlpatterns = [
    path('Login/',          Login           ),
    path('Register/',       Register        ), 
    path('',                Home            ),
    path('Terry/',          Terry           ),
    path('Terry/Trivia/',   Trivia          ),
    path('Terry/Skins/',    Skins           ),
    path('Terry/Consejos/', Consejos        ),
]
