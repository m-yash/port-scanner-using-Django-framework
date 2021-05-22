from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^Light scan',views.scan,name="script"), 
    url(r'^Range Scan',views.rangeScan,name="range"),
]