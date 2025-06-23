from django.db import models
from common.models import CommonModel
# 게시글
# - title
# - content
# - writer
# - date

class Board(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)    
    
    def __str__(self):
        return self.title
