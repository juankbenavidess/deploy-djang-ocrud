from django.urls import path, include
from tasks import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('signup/', views.signup, name='signup'),
    path('task/create/', views.createtask, name='createtask'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.completeTask, name='complete_task'),
    path('tasks/<int:task_id>/deleted', views.deleteTask, name='deleted_task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name="signin"),
    path('tasks/', views.tasks, name = "tasks"),
    path('tasks/completed', views.tasks_completed, name = "tasks_completed")
]