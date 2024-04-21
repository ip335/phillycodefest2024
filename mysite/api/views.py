from django.shortcuts import render
from rest_framework import generics, status
from .models import Test, Question
from .serializers import TestSerializer, QuestionSerializer, ResultSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.
class TestListCreate(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        Test.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = "pk"

class TestList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title", "")

        if title:
            Tests = Test.objects.filter(title__icontains=title)
        else:
            Tests = Test.objects.all()

        serializer = TestSerializer(Tests, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class ResultList(APIView):
    def get(self, request, format=None):
        Results = Test.objects.all()
        serializer = ResultSerializer(Results, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        return Response(status.HTTP_200_OK)