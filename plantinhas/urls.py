"""plantinhas URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('plantas/cadastrar/<int:codigo>', views.plantasCad),
    path('plantas/<int:codigo>', views.plantas),
    path('jardim/cadastro/<int:codigo>', views.jardimCad),
    path('usuario/<int:codigo>', views.usuario),
    path('jardim/plantas/<int:codigo>/<int:jardim>', views.plantadas)
]
