from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

from refeitorioApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('refi/', views.refi, name='refi'),
    path('',views.new_aluno, name='new_aluno'),
    path('editar_aluno/<str:id>', views.editar_aluno, name='editar_aluno'),
    path('excluir_aluno/<str:id>', views.excluir_aluno, name='excluir_aluno'),
    path('',include('userApp.urls')),
    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
