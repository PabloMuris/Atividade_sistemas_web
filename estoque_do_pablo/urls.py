"""
URL configuration for estoque_do_pablo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
]