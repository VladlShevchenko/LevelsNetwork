from rest_framework import serializers
from src.profiles.serializers import UserByFollowerSerializer
from .models import Follower


class ListFollowerSerializer(serializers.ModelSerializer):

    subscribers = UserByFollowerSerializer(many=True, read_only=True)
    subscriber = serializers.ReadOnlyField(source='subscriber.username')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Follower
        fields = ('id', 'subscribers', 'subscriber', 'user')


