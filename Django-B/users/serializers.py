from rest_framework.serializers import ModelSerializer 
from .models import User

class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("username", "email", "is_superuser")