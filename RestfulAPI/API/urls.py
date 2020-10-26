from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', views.TaskList)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls'))
    # path('', views.apiOverview, name='api_overview'),
    # path('task-list/', views.TaskList, name="task-list"),
    # path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    # path('task-create/', views.taskCreate, name="task-create"),
    # path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    # path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]