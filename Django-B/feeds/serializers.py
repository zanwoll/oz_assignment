from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer
# (1) 전체 데이터를 다 보여주는 Serialize

class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True)
    review_set = ReviewSerializer(many=True,read_only=True)
    
    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1