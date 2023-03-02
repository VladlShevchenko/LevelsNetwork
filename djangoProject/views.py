from django.http import HttpResponse


def article(request):
    return HttpResponse('<h3> Articles </h3>')


def article_year(request, year: int):
    return HttpResponse(f'<h3> Articles from {year} </h3>')
