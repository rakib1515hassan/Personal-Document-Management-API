from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from Account.models import Documents

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class DocumentsSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    
    class Meta:
        model = Documents
        fields = '__all__'




class DocumentsSharingSerializers(serializers.HyperlinkedModelSerializer):

    user = UserSerializers(read_only=True)
    sharing_document = serializers.HyperlinkedIdentityField(view_name='documents-sharing', lookup_field = 'title')
    
    class Meta:
        model = Documents
        fields = ['id', 'sharing_document', 'title', 'user', 'description', 'file', 'file_format']
        



















# class DocumentsSerializers(serializers.HyperlinkedModelSerializer):
#     user = UserSerializers(read_only=True)

#     class Meta:
#         model = Documents
#         fields = ['id', 'url', 'title', 'user', 'description', 'file', 'file_format']

#         # Add this line to specify the view name for the URL field
#         extra_kwargs = {
#             'url': {
#                 'view_name': 'documents-sharing', 
#                 'lookup_field': 'title',
#                 }
#         }


    """
    আমরা যদি url এইভাবে বলে দেই তবে আমদের class Meta উপরে url উল্লেখ করার দরকার নেই, but আমরা যদি url এর পরিবর্তে
    sharing_document কথাটি লিখতে চাই তবে আমাদের,
            sharing_document = serializers.HyperlinkedIdentityField(view_name='documents-sharing', lookup_field='title')

    অথবা, 
        sharing_document = serializers.HyperlinkedIdentityField(view_name='documents-sharing')

        extra_kwargs = {
        'sharing_document': {
            'lookup_field': 'title',
            }
        }
    আথবা,
        extra_kwargs = {
            'url': {
                'view_name': 'documents-sharing',
                'lookup_field': 'title',
                }
        }
    """
