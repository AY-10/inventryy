from django.contrib import admin
from django.urls import path
from api.views import UserRegistrationView, UserLoginView, landing_page  # Corrected import

urlpatterns = [
    path('', landing_page, name='landing'),  # Map root URL to landing page
    path('admin/', admin.site.urls),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
]
