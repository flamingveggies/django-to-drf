from rest_framework import serializers

from notes_app.models import Note
from django.contrib.auth.models import User

class NestedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'created', 'updated', 'body']

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserSerializer(serializers.ModelSerializer):
    notes = NestedNoteSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'notes']

class NoteSerializer(serializers.ModelSerializer):
    author = NestedUserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = ['id', 'title', 'author', 'created', 'updated', 'body']
