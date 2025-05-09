from django.urls import path
from .views import (
    EmployerListCreateView,
    EmployerRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', EmployerListCreateView.as_view(), name='employer-list-create'),
    path('<int:id>/', EmployerRetrieveUpdateDestroyView.as_view(), name='employer-retrieve-update-destroy'),
]