## filename: views.py (Django view functions)

from django.http import HttpResponse

def index(request):
    # Получить HttpRequest — параметр запроса
    # Выполнить операции, используя информацию из запроса.
    # Вернуть HttpResponse
    return HttpResponse('Hello from Django!')
