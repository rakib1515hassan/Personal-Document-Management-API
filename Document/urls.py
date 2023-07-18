from django.urls import path
from Document import views




urlpatterns = [
    path('document-create/', views.DocumentsCreateAPIView.as_view()),
]