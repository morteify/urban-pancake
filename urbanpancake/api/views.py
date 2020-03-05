from rest_framework import generics
from .models import User, Picture
from .serializers import UserSerializer, PictureSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


class UserList(generics.ListCreateAPIView):
    """
    List all users, or crate a new user
    """
    permission_classes = [
        permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user
    """
    permission_classes = [
        permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PictureList(generics.ListCreateAPIView):
    """
    List all pictures, or create a new picture
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def perform_create(self, serializer):
        userInstance = User.objects.get(username=self.request.user)
        serializer.save(author=userInstance)


class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a picture
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pictures': reverse('picture-list', request=request, format=format)
    })
