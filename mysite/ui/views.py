from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
import sounddevice as sd
import numpy as np
import wave
from pydub import *
import soundfile as sf
from openai import OpenAI
import openai
import spacy
from pathlib import Path
import time
import pygame
import os


# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/api/tests') # Redirect to a home page or wherever
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

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
    return render(response, "home.html", {})