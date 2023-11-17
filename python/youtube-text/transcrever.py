import os
import speech_recognition as sr
import wave

from properties import ARQUIVO, EXTENCAO, IDIOMA

"""Transformar Audio em Texto"""
def transcrever_audio(nome_audio: str) -> str:
    
    with wave.open(ARQUIVO + '.' + EXTENCAO) as wav:
        duration = wav.getnframes() / wav.getframerate()
        duration /= 60

    i = 0
    while(True):

        recognizer = sr.Recognizer()
        with sr.AudioFile(nome_audio) as source:
            base = recognizer.record(source, duration=60, offset=(i*60))
        try:
            texto = recognizer.recognize_google(base, language=IDIOMA)
            print(texto)
        except sr.UnknownValueError:
            texto = ''
            print('Google Speech Recognition NÃO ENTENDEU o audio')
        except sr.RequestError as e:
            texto = ''
            print('Erro ao solicitar resultados do Google Speech Recognition; {0}'.format(e))

        if i > duration:
            break
        else:
            i += 1

    return texto

transcrever_audio(ARQUIVO + '.' + EXTENCAO)
