from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('swap-status/<int:action_item_id>', views.swap_status, name="swap-status")
]

