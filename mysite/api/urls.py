from django.urls import path
from .views import *

urlpatterns = [
    path("tests/", TestListCreate.as_view(), name="test-view-create"),
    path("tests/delete/<int:pk>", TestRetrieveUpdateDestroy.as_view(), name="test-view-update"),
    path("questions/", QuestionListCreate.as_view(), name="question-view-create"),
    path("results/", ResultList.as_view(), name="result-get")
]