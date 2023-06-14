from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    group = request.data.pop('group')
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if group:
            user.groups.add(group)
        return Response({'success': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        response_data = {
            'token': token.key,
            'id': user.pk,
            'username': user.username,
        }
        if user.image:
            response_data['image'] = user.image.url
        else:
            response_data['image'] = None
        groups = []
        if user.groups:
            for g in user.groups.all():
                groups.append(g.name)
            response_data['groups'] = groups
        else:
            response_data['groups'] = None
        
        return Response(response_data)