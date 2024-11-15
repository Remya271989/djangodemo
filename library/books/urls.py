"""
URL configuration for library project.

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
from django.urls import path
from books import views
app_name="books"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('view',views.view,name="View"),
    path('add',views.add,name="Add"),
    path('details/<int:p>',views.details,name="Details"),
    path('delete/<int:p>',views.delete,name="Delete"),
    path('edit/<int:p>',views.edit,name="Edit"),
    ]






