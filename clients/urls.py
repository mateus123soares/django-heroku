"""clients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from .views import list_clients,test_function,special_case_2003,special_case,month_arquive,hello
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('hello/<str:name>/',hello),
    path('article/2003/',special_case_2003),
    path('article/<int:year>/',special_case),
    path('article/<int:year>/<int:month>',month_arquive),
    path('test/',test_function),
    path('admin/', admin.site.urls),
    path('clients/', include('core.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(redirect_field_name='admin/logout'), name='logout')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
