from django.http import HttpResponse


def employee_salary(request, user_id: int):
    return HttpResponse(f'<h3> Employee {user_id} salary history </h3>')


def employee_expense_history(request, user_id: int, year: int):
    return HttpResponse(f'<h3> Employee {user_id}  expenses  by year: {year}</h3>')


def update_financial_info(request):
    return HttpResponse(f'<h3> Financial info updated </h3>')
