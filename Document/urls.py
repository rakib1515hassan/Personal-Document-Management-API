from django.urls import path
from Document import views




urlpatterns = [
    path('user/document-display/', views.UserDocumentsListAPIView.as_view()),

    path('document-retrieve-update-delete/<int:pk>/', views.UserDocumentsRetrieveUpdateDestroyAPIView.as_view()),

    path('admin/document-retrieve/', views.AdminDocumentsListAPIView.as_view()),

    path('admin/document-retrieve-update-delete/<int:pk>/', views.AdminDocumentsRetrieveUpdateDestroyAPIView.as_view()),

    path('convert-document/', views.UserDocumentsUplodeAPIView.as_view()),

    path('download-document/<int:file_id>/<str:doc_format>/', views.DownloadFileView.as_view()),

]