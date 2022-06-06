from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('concept', views.ConceptViewSet)

app_name = 'concept'

urlpatterns = [
    path('', include(router.urls)),
]
