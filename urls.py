from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^a/$', views.SpiderDebugView.as_view()),
]
