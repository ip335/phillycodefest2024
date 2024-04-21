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

client = OpenAI(api_key="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")
nlp = spacy.load("en_core_web_lg")
print("\nLoaded succesfully\n")

#-------------------------------------

def tokenize(answer):
    doc = nlp(answer)
    for token in doc:
        #print(token.text, "-", token.pos_)
        pass
    return token.text.lower()

#-------------------------------------

def play_audio():
    file_path = 'speech.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Sleep for 1 second
    pygame.mixer.music.stop()

#--------------------------------------
def textToSpeech(text):
  speech_file_path = Path("speech.mp3")
  response = client.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input=text
  )

  response.stream_to_file(speech_file_path)

#---------------------------------------
def record():
  #Recording
  duration = 7  # duration in seconds
  samplerate = 44100  # sample rate in hertz
  channels = 1  # number of channels (mono)
  filePath = 'my_audio_file3.wav'

  # Calculate the number of frames
  frames = int(duration * samplerate)

  # Record audio
  myrecording = sd.rec(frames, samplerate=samplerate, channels=channels, dtype='float64')
  print("Recording...")
  sd.wait()  # Wait until recording is finished
  print("Recording finished.")

  # Save the recording as WAV
  wav_file = filePath
  sf.write(wav_file, myrecording, samplerate)

#---------------------------------------
def speechToText(filePath):
  audio_file = open(filePath, "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
  )
  sentence = transcription.text
  return sentence

#----------------------------------------

#For spelling
def checkSpelling(word, sentence):
  #print(sentence)
  parsedSentence = sentence.split(' ')
  #print(parsedSentence)
  for i in parsedSentence:
    for n in i:
      if n == '-':
        finishedWord = i.replace('-', '').lower()
  print(finishedWord)
  if word == finishedWord:
    print('Correct')
  else:
    print('wrong')

#-----------------------------------

#For numbers
def parseSentence(sentence):
  print(f'Sentence: {sentence}')
  doc = nlp(sentence)
  for token in doc:
      if token.like_num:
          print(f'Number: {token.text}')
          token = int(token.text)
           
  if token in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    return token
  else:
    print('Error')


if __name__ == '__main__':

  print("Welcome to the cognitive test, please answer the following questions:\n")
  '''
  questionOne = "Question 1: \nSpell WORLD\n"
  print(questionOne)
  textToSpeech(questionOne)
  play_audio()
  record()
  sentence = speechToText('my_audio_file3.wav')
  checkSpelling("world", sentence)

  questionTwo = "\nQuestion 2:\nWhat is 5 + 2?\n"
  print(questionTwo)
  textToSpeech(questionTwo)
  play_audio()
  record()
  sentence = speechToText('my_audio_file3.wav')
  token = parseSentence(sentence)
  if token == 7:
    print("Correct")
  else:
    print("Wrong")
  
  '''
  
  questionOne = "What year is this?" 
  print(questionOne)
  textToSpeech(questionOne)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  correctAnswer = 2024
  answerTokenized = tokenize(answer)
  answerTokenized = int(answerTokenized)
  print(f'Your answer: {answerTokenized}')
  print(f'Correct answer: {correctAnswer}')
  if answerTokenized == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")


  questionTwo = "What season is it?"
  print(questionTwo)
  textToSpeech(questionTwo)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  correctAnswer = "spring"
  answerTokenized = tokenize(answer)
  print(f'Your answer: {answerTokenized}')
  print(f'Correct answer: {correctAnswer}')
  if answerTokenized == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  questionThree = "What month is it?"
  print(questionThree)
  textToSpeech(questionThree)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  correctAnswer = "april"
  answerTokenized = tokenize(answer)
  print(f'Your answer: {answerTokenized}')
  print(f'Correct answer: {correctAnswer}')
  if answerTokenized == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  #Fix - extract day number
  '''
  questionFour = "What is today’s date?"
  record()
  answer = speechToText('my_audio_file3.wav')
  correctAnswer = "april 20, 2024"
  answerTokenized = tokenize(answer)
  print(f'Your answer: {answerTokenized}')
  print(f'Correct answer: {correctAnswer}')
  if answerTokenized == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")
'''

  questionFour = "What day of the week is it?"
  print(questionFour)
  textToSpeech(questionFour)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  correctAnswer = "saturday"
  answerTokenized = tokenize(answer)
  print(f'Your answer: {answerTokenized}')
  print(f'Correct answer: {correctAnswer}')
  if answerTokenized == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  questionFive = "What country are we in?"
  print(questionFive)
  textToSpeech(questionFive)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  correctAnswer = "america"
  answerTokenized = tokenize(answer)
  print(f'Your answer: {answerTokenized}')
  print(f'Correct answer: {correctAnswer}')
  if answerTokenized == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  questionSix = "What state are we in?"
  print(questionSix)
  textToSpeech(questionSix)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  correctAnswer = "pennsylvania"
  answerTokenized = tokenize(answer)
  print(f'Your answer: {answerTokenized}')
  print(f'Correct answer: {correctAnswer}')
  if answerTokenized == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  questionSeven = "What city/town are we in?"
  print(questionSeven)
  textToSpeech(questionSeven)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  correctAnswer = "philadelphia"
  answerTokenized = tokenize(answer)
  print(f'Your answer: {answerTokenized}')
  print(f'Correct answer: {correctAnswer}')
  if answerTokenized == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  questionEight = "Repeat these 3 objects: Dog, Cat, Mouse. Remember what they are because you will be asked about them later"
  print(questionEight)
  textToSpeech(questionEight)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav').lower()
  answer = answer.replace('.','')
  answer = answer.replace(',','')
  correctAnswer = "dog cat mouse"
  #answerTokenized = tokenize(answer)
  print(f'Your answer: {answer}')
  print(f'Correct answer: {correctAnswer}')
  if answer == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  questionNine = "Spell the word WORLD"
  print(questionNine)
  textToSpeech(questionNine)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  parsedSentence = answer.split(' ')
  correctAnswer = "world"
  for i in parsedSentence:
    for n in i:
      if n == '-':
        #print(f'spelled word: {i}')
        finishedWord = i.replace('-', '').lower()
  print(finishedWord)
  if correctAnswer == finishedWord:
    print('correct')
  else:
    print('wrong')
  
  questionTen = "Spell the word world BACKWARDS"
  print(questionTen)
  textToSpeech(questionTen)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav')
  parsedSentence = answer.split(' ')
  correctAnswer = "dlrow"
  for i in parsedSentence:
    for n in i:
      if n == '-':
        #print(f'spelled word: {i}')
        finishedWord = i.replace('-', '').lower()
  print(finishedWord)
  if correctAnswer == finishedWord:
    print('correct')
  else:
    print('wrong')

  questionEleven = "please repeat the 3 words I told you to remember earlier"
  print(questionEleven)
  textToSpeech(questionEleven)
  play_audio()
  record()
  answer = speechToText('my_audio_file3.wav').lower()
  answer = answer.replace('.','')
  answer = answer.replace(',','')
  correctAnswer = "dog cat mouse"
  #answerTokenized = tokenize(answer)
  print(f'Your answer: {answer}')
  print(f'Correct answer: {correctAnswer}')
  if answer == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  #



  #SHOW PENCIL, ASK THEM TO TELL YOU WHAT IT IS


  #

  questionTwelve = "Please repeat after me, no ifs or buts allowed. Answer must be exact"
  print(questionTwelve)
  textToSpeech(questionTwelve)
  play_audio()
  print("my name is daniel")
  record()
  answer = speechToText('my_audio_file3.wav').lower()
  correctAnswer = "my name is daniel"
  #answerTokenized = tokenize(answer)
  print(f'Your answer: {answer}')
  print(f'Correct answer: {correctAnswer}')
  if answer == correctAnswer:
      print("Correct")
  else:
      print("Incorrect")

  #Raise hand question

