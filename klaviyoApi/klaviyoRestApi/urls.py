from django.urls import path
from .views import NewUserView

urlpatterns = [
    path('newusers/', NewUserView.as_view(), name='new-users'),
]
