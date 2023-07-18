from django.shortcuts import render
from Account.models import Documents

from Document.serializers import DocumentsSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
# URL = ( http://127.0.0.1:8000/document/document-create/ )
class DocumentsCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsSerializers


# class DocumentsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = DocumentsSerializers

#     def get_queryset(self):
#         user_id = self.kwargs['pk']
#         return Documents.objects.filter()
