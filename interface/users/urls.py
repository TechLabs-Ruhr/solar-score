# users/urls.py

from django.urls import include, path
from .views import UserListView

urlpatterns = [
path('', UserListView.as_view()),
path('auth/', include('dj_rest_auth.urls')),    
path('auth/register/', include('dj_rest_auth.registration.urls'))
]
