from rest_framework import generics
from .models import User, Picture
from .serializers import UserSerializer, PictureSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListCreateAPIView):
    """
    List all users, or crate a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PictureList(generics.ListAPIView):
    """
    List all pictures, or create a new picture
    """
    permission_clsses = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PictureDetail(generics.RetrieveAPIView):
    """
    Retrieve, update or delete a picture
    """
    permission_clsses = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Picture.objects.all()
    serializer_class = UserSerializer
