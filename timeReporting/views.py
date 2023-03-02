from django.http import HttpResponse


def employee_tracked_time(request, week_id: int):
    return HttpResponse(f'<h3> Employee tracked time by week {week_id}</h3>')


def report_time(request):
    return HttpResponse(f'<h3> Work time reported </h3>')


def update_time_tracking(request, user_id: int, date: int):
    return HttpResponse(f'<h3> Time report for date: {date} and user: {user_id} updated </h3>')


def delete_time_tracking(request, user_id: int, date: int):
    return HttpResponse(f'<h3> Time report for date: {date} and user: {user_id} deleted </h3>')
