from django.urls    import path
from Login.views    import Login
from Register.views import Register
from MainPG.views   import Home

urlpatterns = [
    path('Login/',    Login   ),
    path('Register/', Register), 
    path('',          Home    ),

]
