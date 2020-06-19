from django.urls import path
from . import views
urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]
