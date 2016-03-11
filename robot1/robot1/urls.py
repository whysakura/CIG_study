"""robot1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from app1 import views as view1
urlpatterns = [
	url(r'^car_sta/$',view1.car_sta,name='car_sta'),
    url(r'^ceshi/$',view1.ceshi,name='ceshi'),
    url(r'^err_show/$',view1.err_show,name='err_show'),
    url(r'^show/(\d{1})/$',view1.show,name='show'),
    url(r'^test/$',view1.test,name='test'),
	url(r'^time/$',view1.timee,name='timee'),
    url(r'^admin/', admin.site.urls),
]
