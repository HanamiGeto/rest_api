from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Todo
# from rest_framework import CurrentUserDefault

# class UserSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'username', 'email']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    # user = CurrentUserDefault() 
    user = serializers.PrimaryKeyRelatedField(read_only='True', default=serializers.CurrentUserDefault())

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at', 'user', 'time_passed']