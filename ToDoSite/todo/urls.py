from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('swap-status/<int:task_id>', views.swap_status, name="swap-status"),
    path('delete-task/<int:task_id>', views.delete_task, name="delete-task"),
    path('add-task/<str:task_type>', views.add_task, name="add-task"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('logout', views.logout_request, name='logout')
]

