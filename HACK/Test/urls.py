from django.urls import path, include
from .views import auth, Form, form
from . import views
from .views import userAPIView, Stats

urlpatterns = [
    path('', views.auth, name="auth"),
    path('stat/', Stats.as_view(), name="statistic"),
    path('form/', views.form, name="form"),
    path('api/user', userAPIView.as_view(), name="user"),
]
