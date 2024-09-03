from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse(render(request, "index.html"))
