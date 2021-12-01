from django.urls import path
from . import views
from rest_framework.authtoken import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
]
