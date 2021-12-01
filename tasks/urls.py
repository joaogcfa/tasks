from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:pk>', views.task_detail, name='task_detail'),
    path('tasks/', views.get_task, name='get_tasks')
]
