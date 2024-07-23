from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("test/", views.get, name='get_data'),
    path("form/<str:type>/<str:day>/", views.addData, name='add'),
]
