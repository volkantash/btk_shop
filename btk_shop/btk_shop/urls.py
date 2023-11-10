"""
URL configuration for btk_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.apps import apps
import importlib

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('product.urls')),
]

uyg = [uygulama.name for uygulama in apps.get_app_configs()]
uyg2 = apps.get_app_configs()
print(uyg2)
# for i in uyg:
#     try:
#         importlib.import_module(i + '.urls')
#         urlpatterns.append(path('', include(i + '.urls')))
#     except ImportError:
#         pass # print("BulaMADIK " + i + '.urls')

# print(urlpatterns)