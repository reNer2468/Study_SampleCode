from django.conf.urls import url
from . import views

app_name="analize_data"
urlpatterns = [
    url('', views.index, name='index'),
]
