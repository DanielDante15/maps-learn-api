from django.urls import path, include
from django.contrib import admin
from home.views import *

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
# #     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.



urlpatterns = [
    path('', include('home.urls')),
    path('admin/',  admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]