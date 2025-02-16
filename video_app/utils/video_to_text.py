from moviepy.video.io.VideoFileClip import VideoFileClip
import speech_recognition as sr
import os

def extract_audio_from_video(video_path, audio_path="media/extracted_audio.wav"):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path

def transcribe_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Audio not clear"
        except sr.RequestError:
            return "API error"

def video_to_text(video_path):
    audio_path = extract_audio_from_video(video_path)
    text = transcribe_audio_to_text(audio_path)
    os.remove(audio_path)
    return text
