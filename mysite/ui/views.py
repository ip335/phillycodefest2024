from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Audio
from .forms import *
from django.conf import settings
from .ai import *
from django.http import HttpResponseServerError, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import tempfile
import glob

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def register(response):
    form = RegisterForm()
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
        else:
            form = RegisterForm()
    return render(response, "register.html", {"form": form})

def home(response):
    audio_url = settings.MEDIA_URL + "speech.mp3"  # Adjust the file name as necessary
    context = {'audio_url': audio_url}
    return render(response, "home.html", context)

@csrf_exempt
def get_question_audio_url(response):
    if response.method == "POST":
        json_data = json.loads(response.body)
        try:
            question = json_data['question']
        except KeyError:
            HttpResponseServerError("Malformed data!")
        path = textToSpeech(question)
        return JsonResponse({'audio_url': str(path)})

@csrf_exempt
def get_answer_url(response):
    if response.method == "POST":
        file = response.FILES.get("audio")
        audio = Audio(record=file)
        list_of_files = glob.glob('media/*')
        for paths in list_of_files:
            if paths.startswith("record"):
                os.remove(paths)
        audio.save()
        list_of_files = glob.glob('media/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        result = speechToText(latest_file)
        answer = tokenize(result)

        return JsonResponse({"answer": answer})
    else:
        return JsonResponse({'status': 'error'})

def test(response):
    return render(response, "test.html", {})