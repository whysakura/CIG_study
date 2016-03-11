"""one URL Configuration

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
from  app1 import views
urlpatterns = [
    url(r'^show/$',views.show,name='show'),
	url(r'^sh/$',views.sh,name='sh'),
	url(r'^a/(\d+)/(\d+)$',views.new_get,name='new_get'),#重定向到b
	url(r'^b/(\d+)/(\d+)$',views.get,name='get'),#调用get视图
	url(r'^aa/$',views.aa,name='aa'),
	url(r'^bb/$',views.bb,name='bb'),
    url(r'^admin/', admin.site.urls),
]
