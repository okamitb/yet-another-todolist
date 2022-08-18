from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('swap-status/<int:action_item_id>', views.swap_status, name="swap-status"),
    path('delete-action-item/<int:action_item_id>', views.delete_action_item, name="delete-action-item"),
    path('add-action-item', views.add_action_item, name="delete-action-item")
]

