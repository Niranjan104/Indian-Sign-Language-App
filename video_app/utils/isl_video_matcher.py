import os
import numpy as np
from sentence_transformers import SentenceTransformer

#  Load AI model to compare words
model = SentenceTransformer('all-MiniLM-L6-v2')

#  Get all available ISL videos
VIDEO_FOLDER = "media/"
video_files = [file.replace(".mp4", "").lower() for file in os.listdir(VIDEO_FOLDER) if file.endswith(".mp4")]
video_embeddings = model.encode(video_files)

#  AI-powered function to find the best match
def find_best_match(input_word):
    input_vector = model.encode([input_word])
    similarities = np.dot(video_embeddings, input_vector.T).flatten()
    best_match_index = np.argmax(similarities)
    
    #  Return best-matching ISL video (if similarity > 0.5)
    return video_files[best_match_index] if similarities[best_match_index] > 0.5 else None
