from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import authenticate

from Account.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer, 
    UserProfileSerializer, 
    UserChangePasswordSerializer, 
    SendPasswordResetEmailSerializer, 
    UserPasswordResetSerializer,
)

from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated, 
)

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


# NOTE ------------( Creating tokens manually )------------------------------------------
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# NOTE ------------------( User Registration View )-------------------------------------
# URL = ( http://127.0.0.1:8000/auth/register/ )
class UserRegistrationView(APIView):

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)   ## Token Genaret
            return Response({'token': token,'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#_________________________________________________________________________________________




# NOTE ------------------------( User Login View )----------------------------------------
# URL = ( http://127.0.0.1:8000/auth/login/ )
class UserLoginView(APIView):

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
        
            try:
                usr = User.objects.get(email = email)
                if usr:
                    authenticate(username= usr.username , password=password)
                    token = get_tokens_for_user(usr)   ## Token Genaret           
                    return Response({'token': token,'msg':'Login Success'}, status=status.HTTP_200_OK)
                
            except User.DoesNotExist:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#_________________________________________________________________________________________
# NOTE ------------------------( User Profile View )--------------------------------------
# URL = ( http://127.0.0.1:8000/auth/profile/ )
class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#______________________________________________________________________________________



# NOTE ------------------------( ChangePasswor View )----------------------------------
# URL = ( http://127.0.0.1:8000/auth/change-password/ )
class UserChangePasswordView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password is successfully changed.'}, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#______________________________________________________________________________________




# NOTE -----------------( Passord Reset Email Send With Link/OTP View )----------------

# NOTE OTP send in Email
# URL = ( http://127.0.0.1:8000/auth/reset-password-email-send/ )
class SendPasswordResetEmailView(APIView):

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
    


# NOTE OTP Verification
# URL = ( http://127.0.0.1:8000/auth/reset-password-email-verify/ )
class UserPasswordResetView(APIView):

    def post(self, request, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
    
#______________________________________________________________________________________