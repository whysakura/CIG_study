"""rob_test2 URL Configuration

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
from test2 import views as test2_views 

urlpatterns = [
    # url(r'^get_car/$',test1_views.get_car,name='get_car'),
    url(r'^ask/$',test2_views.ask,name='ask'),#提交订单
    url(r'^show_order/$',test2_views.show_order,name='show_order'),#显示订单
    url(r'^over_order/$',test2_views.over_order,name='over_order'),#over订单
    url(r'^show_data/$',test2_views.show_data,name='show_data'),#ajax返回数据
    url(r'^show_car/$',test2_views.show_car,name='show_car'),#显示小车路线
    url(r'^car_sta/$',test2_views.car_sta,name='car_sta'),#收集小车状态
    url(r'^admin/', admin.site.urls),
]
