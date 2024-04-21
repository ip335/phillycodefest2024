from rest_framework import serializers
from .models import *

class TestSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   

    class Meta:
        model = Test
        fields = ['id','name', 'date', 'questions', 'result']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'date', 'result']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'answer', 'test']
