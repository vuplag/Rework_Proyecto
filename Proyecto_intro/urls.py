from django.urls    import path
from Login.views    import Login,nigga
from Register.views import Register

urlpatterns = [
    path('Login/',    Login),
    path('Register/', Register), 

]
