from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employer
from .serializers import EmployerSerializer
from users_app.models import CustomUser

class EmployerListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)