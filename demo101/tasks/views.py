from django.http import HttpResponse
from django.shortcuts import render

from demo101.tasks.models import Task


# Create your views here.


def index_old(request):
    name = request.GET.get('name', 'NONAME')
    content = "<h1>Hello!!</h1>" + \
                f"<p>My first demo, {name}!</p>" + \
                "<ul><li>1</li><li>2</li></ul>"
    return HttpResponse(content)


# # DB view:
def index_db_no_template(request):
    title_filter = request.GET.get('filter', '')
    # the filter is passed in the URL: http://127.0.0.1:8000/?filter=mess

    tasks = Task.objects.all()

    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter)

    if not tasks:
        return HttpResponse("<h1>No tasks!</h1>")
    result = []
    for task in tasks:
        result.append(
            f"""
            <li>
                <h2>{task.title}</h2>
                <p>{task.description}</p>
            </li>
        """)
    ul = f"<ul>{''.join(result)}</ul>"
    content = f"""
    <h1>{tasks.count()} Tasks</h1>
    {ul}
    """
    return HttpResponse(content)


# DB view with templates:
def index(request):
    title_filter = request.GET.get('title_filter', '')
    # the filter is passed in the URL: http://127.0.0.1:8000/?filter=mess
    tasks = Task.objects.all()

    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter.lower())

    context = {
        'title': 'The tasks app with DB and Templates!',
        'tasks_list': tasks,
        'tasks_count': tasks.count(),
        'title_filter': title_filter,
    }
    return render(request,
                  'tasks/index.html',
                  context,
                  )
