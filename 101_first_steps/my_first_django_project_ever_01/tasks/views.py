from lib2to3.fixes.fix_input import context

from django import http
from django.shortcuts import render

from my_first_django_project_ever_01.tasks.models import Task

'''
FBV
1. A function that has one or more parameters
2. Return a response
'''


# def index(request):
#     name = request.GET.get('name', 'no name')
#     content = "<h1>Hello</h1>" + \
#               f"<p>alabala, my name is {name}</p>" + \
#               (
#                   "<ul>"
#                   "<li>1</li>"
#                   "<li>2</li>"
#                   "<li>3</li>"
#                   "</ul>"
#               )
#     return http.HttpResponse(content)

# def index(request):
#     title_filter = request.GET.get('filter', None)
#
#     tasks = Task.objects.all()
#
#     if title_filter:
#         tasks = tasks.filter(title__icontains=title_filter.lower())
#
#     if not tasks:
#         return http.HttpResponse("<h1>No tasks yet!</h1>")
#
#     result = []
#
#     for task in tasks:
#         result.append(f"""
#         <li>
#             <h2>{task.title}</h2>
#             <p>{task.description}</p>
#         </li>
#         """)
#
#     ul = f"<ul>{''.join(result)}</ul>"
#
#     content = f"""
#     <h1>{len(tasks)} Tasks</h1>
#     {ul}
#     """

# return http.HttpResponse(content)
def index(request):
    title_filter = request.GET.get('title_filter', '')
    tasks = Task.objects.all()

    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter.lower())

    context = {
        'title': 'the task app',
        'task_list': tasks,
        'task_list__count': tasks.count(),
        'title_filter': title_filter,
    }
    return render(request,
                  'tasks/index.html',
                  context, )
