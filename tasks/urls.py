from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('GET', views.get_tasks, name='get_tasks'),
    path('ADD', views.post_task, name='post_task'),
    path('DELETE', views.del_task, name='del_task'),
]
