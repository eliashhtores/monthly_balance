from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('finance', views.FinanceViewSet)

app_name = 'finance'

urlpatterns = [
    path('', include(router.urls)),
]
