from django.db import models

# 게시글
# - title
# - content
# - writer
# - date

class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
