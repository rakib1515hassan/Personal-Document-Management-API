from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from Account.models import Documents



class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'