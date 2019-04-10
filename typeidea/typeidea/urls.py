"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from blog.views import post_list, post_detail
from config.views import links
from typeidea.custom_site import custom_site


urlpatterns = [
    path('', post_list),
    path('category/<category_id>', post_list),
    path('tag/<tag_id>', post_list),
    path('post/<post_id>.html', post_detail),
    path('links', links),
    path('super_admin/', admin.site.urls),
    path('admin/', custom_site.urls),
]
