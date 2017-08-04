from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /register/
    url(r'^register', views.register, name='register'),
]
