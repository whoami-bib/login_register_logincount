from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([AllowAny])
def validate_token(request):
    refresh_token = request.data.get('refresh_token')
    if refresh_token:
        try:
            token = RefreshToken(refresh_token)
            token.verify()
            return Response({'message': 'Token is valid'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Token not provided'}, status=status.HTTP_401_UNAUTHORIZED)

# Custom token views to use email instead of username
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = self.user
            user.login_count += 1
            user.save()
        return response

class CustomTokenRefreshView(TokenRefreshView):
    pass

@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        user = serializer.save()
        password = request.data.get('password')
        user.set_password(password)
        user.save()
        print("_____________________")
        print(user.email,user.password,user.is_admin)
        print("_____________________")
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email')
    print(email)

    password = request.data.get('password')
    print(password)
    user1=CustomUser.objects.all()
    print(user1)
    user = CustomUser.objects.filter(email=email).first()


    if user is None or not check_password(password, user.password):
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    # Increment login_count
    user.login_count += 1
    user.save()

    refresh = RefreshToken.for_user(user)
    data = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([])
def home_page(request):
    print("___________________")
    print(request)
    user = request.user
    print("user:",user)
    data = {
        'email': user.email,
        'login_count': user.login_count,
        'is_admin':user.is_admin,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_login_count_view(request):
    if request.user.is_admin:
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Permission denied. You must be an admin.'}, status=403)
