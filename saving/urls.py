from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('saving', views.SavingViewSet)
router.register('saving-detail', views.SavingDetailViewSet)

app_name = 'saving'

urlpatterns = [
    path('', include(router.urls)),
]
