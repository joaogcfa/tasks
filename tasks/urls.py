from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:pk>', views.delete_task, name='delete_task'),
    path('tasks/', views.get_or_post, name='get_or_post')
]
