from empleos import views
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

urlpatterns = [
    path('usuarios/', views.UsuarioList.as_view()),
    path('usuarios/<int:pk>', views.UsuarioDetail.as_view()),
    path('empleos/', views.EmpleoList.as_view()),
    path('empleos/<int:pk>', views.EmpleoDetail.as_view()),
    path('verpostulaciones/', views.VerPostulacionList.as_view()),
    path('postulaciones/', views.PostulacionList.as_view()),
    path('postulaciones/<int:pk>', views.PostulacionDetail.as_view()),
    path('categorias/', views.CategoriaList.as_view()),
    path('categorias/<int:pk>', views.CategoriaDetail.as_view()),
    path('', include(router.urls)),
]