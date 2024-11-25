from django.urls    import path
from Login.views    import Login
from Register.views import Register
from MainPG.views   import Home
from Terry.views   import Terry
urlpatterns = [
    path('Login/',    Login   ),
    path('Register/', Register), 
    path('',          Home    ),
    path('Terry/',    Terry   ),
]
