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
from timeReporting.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('report/<int:week_id>/', employee_tracked_time),
    path('report/', report_time),
    path('update/<int:user_id>/<int:date>', update_time_tracking),
    path('delete/<int:user_id>/<int:date>', delete_time_tracking),

]
