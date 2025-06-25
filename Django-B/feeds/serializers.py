from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
# (1) 전체 데이터를 다 보여주는 Serialize

class FeedSerializer(ModelSerializer):
    
    user = FeedUserSerializer()
    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1