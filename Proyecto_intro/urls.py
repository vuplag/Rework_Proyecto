from django.urls    import path
from Login.views    import Login
from Register.views import Register
from MainPG.views import MainPG
urlpatterns = [
    path('Login/',    Login),
    path('Register/', Register),
    path('', MainPG) 

]
