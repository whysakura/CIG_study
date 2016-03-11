from django.conf.urls import url
from app1 import views as app1_views
urlpatterns=[
	url(r'^app1/$',app1_views.app2,name='app2'),
	url(r'^app1/(\d+)/(\d+)$',app1_views.new_get,name='new_get'),#重定向到b
	url(r'^app2/(\d+)/(\d+)$',app1_views.get,name='get'),#调用get视图
]