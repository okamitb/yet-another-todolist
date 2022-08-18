from django.shortcuts import render, redirect
from .models import ActionItem
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    todo_list = ActionItem.objects.all().order_by("id")
    context = {"list": todo_list}
    return render(request, "todo/index.html", context)


def swap_status(request, action_item_id):
    item = ActionItem.objects.get(id=action_item_id)
    item.swap_status()
    return redirect(index)


def delete_action_item(request, action_item_id):
    item = ActionItem.objects.get(id=action_item_id)
    item.delete()
    return redirect(index)


@csrf_exempt
def add_action_item(request):
    new_action_item_text = request.POST['action-item-text']
    item = ActionItem(text=new_action_item_text, completed=False)
    item.save()
    return redirect(index)
