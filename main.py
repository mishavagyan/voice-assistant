import speech_recognition as sr
import pyaudio

recognizer = sr.Recognizer() 

while True:

    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio = recognizer.listen(mic)
            # for russian
            text = recognizer.recognize_google(audio, language="ru-Ru")
            text = text.lower()

            print(f"Recognized text:\n{text}") 

    except KeyboardInterrupt:
        break

    except sr.UnknownValueError:
        recognizer = sr.Recognizer() 
        continue
