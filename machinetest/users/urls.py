from django.urls import path
from .views import CustomTokenObtainPairView, CustomTokenRefreshView
from .views import user_registration, user_login, home_page,user_login_count_view

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    path('register/', user_registration, name='user-registration'),
    path('login/', user_login, name='user-login'),
    path('home/', home_page, name='home-page'),
    path('login-count/', user_login_count_view, name='user-login-count'),
]
