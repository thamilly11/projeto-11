"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from aluno.views import (
    aluno_criar,
    aluno_detail,
    index,
    aluno_listar,
    aluno_editar,
    aluno_remover,
    curso_listar,
    curso_criar,
    cidade_listar,
    cidade_criar,
    cidade_editar,
    cidade_remover,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("aluno/", aluno_criar, name="aluno_criar"),
    path("aluno/editar/<int:id>/", aluno_editar, name="aluno_editar"),
    path("aluno/remover/<int:id>/", aluno_remover, name="aluno_remover"),
    path("aluno/listar", aluno_listar, name="aluno_listar"),
    path("aluno/detalhes/<int:pk>/", aluno_detail, name="aluno_detail"),
    path("curso/listar/", curso_listar, name="curso_listar"),
    path("curso/criar/", curso_criar, name="curso_criar"),
    path("cidade/criar/", cidade_criar, name="cidade_criar"),
    path("cidade/listar/", cidade_listar, name="cidade_listar"),
    path("cidade/editar/<int:id>/", cidade_editar, name="cidade_editar"),
    path("cidade/remover/<int:id>/", cidade_remover, name="cidade_remover"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
