from django.urls import path, include
from django.contrib import admin
from home.views import *
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('',include('home.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/',  admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]