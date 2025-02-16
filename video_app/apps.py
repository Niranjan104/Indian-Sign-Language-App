from django.apps import AppConfig
from video_app.utils.trie import Trie 
import os

class VideoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video_app'

    def ready(self):
        from .utils.isl_video_matcher import video_files  # Load video file list

        # Initialize Trie globally
        global isl_trie
        isl_trie = Trie()
        for file in video_files:
            isl_trie.insert(file, f"media/{file}.mp4")  # Store full path
