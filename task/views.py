from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


# Create your views here.
@api_view(['GET'])
def index(request):
    api = {
        'create new user' : 'task/new',
        'view all' : 'task/all',
    }
    return Response(api)

@api_view(['GET'])
def taskAll(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskNew(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)