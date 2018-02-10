from django.conf.urls import url
from . import views

app_name = "users"

urlpatterns = [
    # url(r"^$", views.index, name="index"),
    url(r"^register/$", views.register, name="register"),
    url(r"^login/$", views.user_login, name="user_login"),
    url(r'^validate_username/$', views.validate_username, name='validate_username'),

]