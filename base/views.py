from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def home(request):
    todo_objs = Todo.objects.all()
    data = {'todos':todo_objs}
    return render(request, 'index.html', context = data)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Todo.objects.create(name=name, description=description, status=status)

        return redirect('home')

    return render(request, 'create.html')


def edit(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo_obj.name = request.POST.get('name')
        todo_obj.description = request.POST.get('description')
        todo_obj.status = request.POST.get('status')

        todo_obj.save()
        return redirect('home')

    data_dict = {'todo': todo_obj}
    return render(request, 'edit.html', context=data_dict)

def delete(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect('home')


