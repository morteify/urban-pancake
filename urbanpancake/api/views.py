from rest_framework import generics
from .models import User, Picture
from .serializers import UserSerializer, PictureSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


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
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
