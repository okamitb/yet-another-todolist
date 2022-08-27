from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.


@login_required
def index(request):
    daily_list = Task.objects.filter(list_type="D").order_by("id")
    weekly_list = Task.objects.filter(list_type="W").order_by("id")
    monthly_list = Task.objects.filter(list_type="M").order_by("id")
    context = {
        "daily_list": daily_list,
        "weekly_list": weekly_list,
        "monthly_list": monthly_list
    }
    return render(request, "todo/index.html", context)


def swap_status(request, task_id):
    item = Task.objects.get(id=task_id)
    item.swap_status()
    return redirect(index)


def delete_task(request, task_id):
    item = Task.objects.get(id=task_id)
    item.delete()
    return redirect(index)


@csrf_exempt
def add_task(request, task_type):
    new_task_text = request.POST['task-text']
    item = Task(text=new_task_text, completed=False, list_type=task_type)
    item.save()
    return redirect(index)


@csrf_exempt
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(login_request)
        else:
            error_text = []
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    form = NewUserForm()
    return render(request=request, template_name="todo/register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(index)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="todo/login.html", context={"login_form": form})

