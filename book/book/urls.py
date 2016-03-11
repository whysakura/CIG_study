"""book URL Configuration

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
from b1 import views as b1_views
urlpatterns = [
	url(r'^add/$',b1_views.add,name='add'),
    url(r'^added/$',b1_views.added,name='added'),
    url(r'^gt/$',b1_views.gt,name='gt'),
    url(r'^pt/$',b1_views.pt,name='pt'),
	# url(r'^pos/(\w+)/$',b1_views.pos,name='pos'),
    url(r'^admin/', admin.site.urls),
]
