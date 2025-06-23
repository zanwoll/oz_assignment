from django.db import models

class CommonModel(models.Model):
    # auto_now_add : 현재 데이터 생성 시간을 기준으로 생성됩니다. -> 이후 데이터가 업데이트 되어도 수정되지 않습니다.
    create_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 생성되는 시간 기준으로 일단 생성됩니다. -> 이후 데이터가 업데이트가 되면 시간도 업데이트된 현재 시간을 기준으로 업데이트 된다.
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True # 데이터베이스의 테이블에 위와 같은 컬럼이 추가되지 않습니다.
