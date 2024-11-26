from django.urls    import path, include
from Login.views    import Login
from MainPG.views   import Home
from Terry.views   import Terry
from Register.views    import Register_view
from Register import views

urlpatterns = [
    path('Login/',    Login   ),
    path('Register/', views.Register_view, name='Register'),
    path('',          Home    ),
    path('Terry/',    Terry   ),
]
