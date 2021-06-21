from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success: Task has been successfully added.")
        return redirect('/')
    
    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def update(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Success: Task has been successfully updated.")
            return redirect('/')
            
    context = {'form':form}
    
    return render(request, 'tasks/update.html', context)

def delete(request, pk):
    item = Tasks.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Success: Task has been successfully deleted.")
        return redirect('/')
    
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)