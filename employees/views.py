from django.http import HttpResponse


def employees(request):
    return HttpResponse('<h3> List of all employees </h3>')


def employees_birthdays(request, month: int):
    return HttpResponse(f'<h3> Employee with birthday in month №{month} </h3>')


def newcomers(request):
    return HttpResponse(f'<h3> Newcomers </h3>')


def employees_by_id(request, user_id: int):
    return HttpResponse(f'<h3> Employee with id {user_id} </h3>')


def employees_add_new(request):
    return HttpResponse(f'<h3> New employee was added </h3>')


def update_employee(request, user_id: int):
    return HttpResponse(f'<h3> Employee with id {user_id} updated </h3>')


def delete_employee(request, user_id: int):
    return HttpResponse(f'<h3> Employee with id {user_id} deleted </h3>')

