from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password

# api/v1/users [POST] => 유저 생성 API
class Users(APIView):
    def post(self, request):
        # password => 검증을 해야하고, 해쉬화해서 저장 필요
        # the other => 비밀번호 외 다른 데이터들
        
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)
        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")
        
        if serializer.is_valid():
            user = serializer.save() # 새로운 유저를 생성
            user.set_password(password) # 비밀번호를 해쉬화
            user.save()
            
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)

# api/v1/users/myinfo [GET, POST]
class MyInfo(APIView):
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, 
                                          data=request.data, 
                                          partial=True)
        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors)