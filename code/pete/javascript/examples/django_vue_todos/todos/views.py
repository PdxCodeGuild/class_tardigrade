from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Todo

def index(request):
    return render(request, 'todos/index.html')

def get_todos(request):
    data = {'todos': []}
    todos = Todo.objects.all()
    for todo in todos:
        todo_dict = {
            'text': todo.text,
            'completed': todo.completed
        }
        data['todos'].append(todo_dict)
    print(data)
    return JsonResponse(data)

def add_new_todo(request):
    data = json.loads(request.body) # request.body is the data property of the axios call
    # it comes in as a string, so json.loads take in that string and returns a python dictionary
    # print(data) # {'text': 'test'}
    text = data.get('text')
    Todo.objects.create(text=text)
    return JsonResponse({'message': 'OK'})