from rest_framework import serializers
from users.models import User


class UserPrimarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
