"""madurez_tecnologica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('encuesta/<int:encuesta>/', login_required(views.encuesta), name='encuesta'),
    path('encuesta2/<int:encuesta>/', views.encuesta, name='encuesta2'),
    path('pregunta/<int:encuesta>/<int:serv>/', login_required(views.pregunta), name='preguntas'),
    path('pregunta2/<int:encuesta>/<int:serv>/', views.pregunta, name='preguntas2'),
    path('singup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('gracias/', views.gracias, name='gracias'),
    path('', views.index2, name='index2'),

]
