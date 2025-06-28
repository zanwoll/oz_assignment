from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import MyInfoUserSerializer

class ReviewSerializer(ModelSerializer):
    user = MyInfoUserSerializer()
    class Meta:
        model = Review
        fields = "__all__"