from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'credential', views.CredentialViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
