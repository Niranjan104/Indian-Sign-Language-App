import speech_recognition as sr

def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)  # Record the entire audio file

        try:
            text = recognizer.recognize_google(audio_data)  # Convert speech to text
            return text
        except sr.UnknownValueError:
            return "Audio not clear"
        except sr.RequestError:
            return "API request error"

