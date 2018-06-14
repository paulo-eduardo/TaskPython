from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from task import views

urlpatterns = [
    url(r'^/$', views.TaskList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)