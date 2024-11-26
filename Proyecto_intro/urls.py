from django.urls    import path, include
from Login.views    import Login
from MainPG.views   import Home
from Terry.views   import Terry
urlpatterns = [
    path('Login/',    Login   ),
    path('Register/', Register), 
    path('',          Home    ),
    path('Terry/',    Terry   ),
]
