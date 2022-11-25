from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        password = request.data.get('password')

        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data.get('password') == serializer.validated_data.get('password_confirm'):
                user = serializer.save()
                user.set_password(password)
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
