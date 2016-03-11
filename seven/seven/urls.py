"""seven URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from app7 import views as app7_views
from app4 import views as app4_views
urlpatterns = [
    url(r'^add/$',app7_views.add,name='add'),
    url(r'^show/$',app7_views.show,name='show'),
    url(r'^tem/$',app7_views.tem,name='tem'),
    url(r'^app7/$',app7_views.app4,name='app4'),
    url(r'^app4/$',app4_views.a,name='a'),
    url(r'^app5/(?P<year>[0-9]{4})/$',app4_views.age,name='age'),
    url(r'^app/$',app4_views.age,{'province':'xg'}),
    url(r'^app4/(?P<page>[0-9]+)$',app4_views.page,name='page'),
    url(r'^admin/', admin.site.urls),
]
