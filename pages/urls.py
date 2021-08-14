from django.urls import path
from django.urls.resolvers import URLPattern
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
]