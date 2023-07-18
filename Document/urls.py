from django.urls import path
from Document import views




urlpatterns = [
    path('document-create/', views.UserDocumentsListCreateAPIView.as_view()),

    path('document-retrieve-update-delete/<int:pk>/', views.UserDocumentsRetrieveUpdateDestroyAPIView.as_view()),

    path('admin/document-retrieve/', views.AdminDocumentsListAPIView.as_view()),

    path('admin/document-retrieve-update-delete/<int:pk>/', views.AdminDocumentsRetrieveUpdateDestroyAPIView.as_view()),

]