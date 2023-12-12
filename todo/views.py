from django.shortcuts import render

#here you type your code

def get_todo_list(request):
    return render(request, 'todo/todo_list.html')