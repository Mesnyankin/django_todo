"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.static import serve
from django.contrib.auth import views as auth_views
from tasks import views as task_views
from users import views as user_views
from tasks.forms import CustomAuthenticationForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Включаем встроенные маршруты аутентификации
    path("register/", user_views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html", authentication_form=CustomAuthenticationForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("tasks/", include("tasks.urls")),  # Подключаем маршруты задач
    path("", task_views.task_list, name="task_list"),  # Главная страница – список задач
]
#Добавляем обработку статики в режиме DEBUG = False
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]