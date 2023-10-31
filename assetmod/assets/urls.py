from django.urls import include, path
from rest_framework import routers
from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'assets', views.AssetViewSet)
router.register(r'transfers', views.TransferViewSet)
router.register(r'repairs', views.RepairViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('login/', views.CustomLogin.as_view()),
    path('', include(router.urls)),
]