from rest_framework import serializers
from .models import User, Picture


class UserSerializer(serializers.ModelSerializer):
    pictures = serializers.HyperlinkedIdentityField(
        many=True, view_name='picture-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'pictures']


class PictureSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Picture
        fields = ['id', 'description', 'publish_date', 'author']
