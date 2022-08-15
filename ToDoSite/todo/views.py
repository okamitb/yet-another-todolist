from django.shortcuts import render, redirect
from .models import ActionItem
# Create your views here.


def index(request):
    todo_list = ActionItem.objects.all().order_by("id")
    context = {"list": todo_list}
    return render(request, "todo/index.html", context)


def swap_status(request, action_item_id):
    item = ActionItem.objects.get(id=action_item_id)
    item.swap_status()
    return redirect(index)
