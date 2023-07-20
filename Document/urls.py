from django.urls import path
from Document import views




urlpatterns = [
    path('user/document-uplode/', views.UserDocumentsUplodeAPIView.as_view()),

    path('user/document-display/', views.UserDocumentsListAPIView.as_view()),

    path('user/document-retrieve-update-delete/<int:pk>/', views.UserDocumentsRetrieveUpdateDestroyAPIView.as_view(), name='documents-detail'),

    path('admin/document-retrieve/', views.AdminDocumentsListAPIView.as_view()),

    path('admin/document-retrieve-update-delete/<int:pk>/', views.AdminDocumentsRetrieveUpdateDestroyAPIView.as_view()),

    

    path('download-document/<int:file_id>/<str:doc_format>/', views.DownloadFileView.as_view()),

]