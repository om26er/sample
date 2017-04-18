from django.conf.urls import url

from sample_app import views

urlpatterns = [url(r'^api/greetings$', views.SimpleView.as_view())]
