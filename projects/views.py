from django.http import HttpResponse


def projects(request):
    return HttpResponse('<h3> List of all projects </h3>')


def project_by_project_id(request, project_id: int):
    return HttpResponse(f'<h3> Project with id {project_id} </h3>')


def team_by_project_id(request, project_id: int):
    return HttpResponse(f'<h3> Team of project with id {project_id} </h3>')
