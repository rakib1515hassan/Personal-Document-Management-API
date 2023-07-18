from django.shortcuts import render
from Account.models import Documents

from Document.serializers import DocumentsSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q


# Create your views here.
# URL = ( http://127.0.0.1:8000/document/document-create/ )
class UserDocumentsListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsSerializers

    def get_queryset(self):
        user = self.request.user  # Get the current user
        return Documents.objects.filter(user=user)




# URL = ( http://127.0.0.1:8000/document/document-retrieve-update-delete/id/ )
class UserDocumentsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsSerializers

    def get_queryset(self):
        user = self.request.user  # Get the current user
        return Documents.objects.filter(user=user)
    





# URL = ( http://127.0.0.1:8000/document/admin/document-retrieve/ )
class AdminDocumentsListAPIView(generics.ListAPIView):
    queryset = Documents.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = DocumentsSerializers





# URL = ( http://127.0.0.1:8000/document/admin/document-retrieve-update-delete/id/ )
class AdminDocumentsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = DocumentsSerializers

    def get_queryset(self):
        user = self.request.user  # Get the current user
        if user.is_superuser == True:
            doc_id = self.kwargs['pk']
            return Documents.objects.filter(pk = doc_id)



