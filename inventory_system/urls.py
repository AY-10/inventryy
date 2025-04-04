from django.contrib import admin
from django.urls import path
# Added UserManagementView
from api.views import UserRegistrationView, UserLoginView, landing_page, UserManagementView

urlpatterns = [
    path('', landing_page, name='landing'),  # Map root URL to landing page
    path('admin/', admin.site.urls),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/users/', UserManagementView.as_view(),
         name='user_management'),  # Added user management endpoint
]
