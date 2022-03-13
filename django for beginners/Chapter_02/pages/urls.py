from django.urls import path
from .views import home_page_view

urlpatterns = [
    path('', home_page_view, name='home'),
    # when the home page requested the function home_page-view() will be executed
]
