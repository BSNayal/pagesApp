from django.urls import path
from .views import homePageView

urlpatterns=[
    path(route='',view=homePageView,name='home')
]