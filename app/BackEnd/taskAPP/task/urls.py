from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from task import views

urlpatterns = [
    url(r'^api/task/$', views.TaskList.as_view()),
    url(r'^api/task/(?P<pk>[0-9]+)/$', views.Task.as_view()),
    url(r'^api/task/status/(?P<pk>[0-9]+)/$', views.TaskStatus.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)