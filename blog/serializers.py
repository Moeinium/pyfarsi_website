from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Comment
from account.models import User


class GetUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class GetCommentSerializer(ModelSerializer):
    author = GetUser(read_only=True)

    class Meta:
        model = Comment
        exclude = ('article',)
        read_only_fields = ('content', 'date', 'status')


class CreateCommentSerializer(ModelSerializer):
    article = PrimaryKeyRelatedField()

    class Meta:
        model = Comment
        exclude = ('date', 'author', 'status')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
