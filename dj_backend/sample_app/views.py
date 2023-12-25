from django.http import HttpResponse


def hello_world(request) -> HttpResponse:
    return HttpResponse("Hello, World!")
