"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from employees.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', employees),
    re_path(r'^birthdays/month=(?P<month>[0-9]{2}/$)', employees_birthdays),
    path('<int:user_id>/', employees_by_id),
    path('newcomers/', newcomers),
    path('add-employee/', employees_add_new),
    path('update/<int:user_id>/', update_employee),
    path('delete/<int:user_id>/', delete_employee),


]
