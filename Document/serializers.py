from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from Account.models import Documents

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# class DocumentsSerializers(serializers.HyperlinkedModelSerializer):
class DocumentsSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    
    class Meta:
        model = Documents
        fields = '__all__'
        # fields = ['id', 'url', 'title', 'user', 'description', 'file', 'file_format']


