from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request, id: int) -> HttpResponse:
    data = {
        "name": "Ranoob",
        "disciplines": ["Dev. Web 2", "Pol. Educacionais", "Sem. Temático"],
        "id": id,
    }
    return HttpResponse(render(request, "index.html", data))
