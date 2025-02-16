import spacy
import string
import os

nlp = spacy.load("en_core_web_sm")
MEDIA_FOLDER = "media"

# Load available video words (handle capitalization properly)
video_words = {file.split(".mp4")[0] for file in os.listdir(MEDIA_FOLDER) if file.endswith(".mp4")}

def preprocess_text(text):
    """Lowercase text and remove punctuation."""
    return text.translate(str.maketrans("", "", string.punctuation))

def video_exists(word):
    """Check if a video exists for a word (handles capitalization)."""
    return word.capitalize() in video_words or word in video_words

def restructure_sentence(doc):
    """
    Restructure the sentence to follow ISL word order.
    ISL typically follows Subject-Object-Verb (SOV) order.
    """
    words = [token.text for token in doc if token.pos_ not in {"AUX", "DET", "PART", "ADP"}]  # Remove unnecessary words

    if len(words) >= 2 and words[-1] in {"am", "is", "are", "was", "were"}:
        words.pop()  # Remove 'is/are' at the end (not needed in ISL)

    return words

def convert_to_isl(text):
    text = preprocess_text(text)
    doc = nlp(text)

    isl_sequence = []
    for sent in doc.sents:
        isl_words = restructure_sentence(sent)
        isl_sentence = []

        for word in isl_words:
            capitalized_word = word.capitalize()  # Match video filenames
            if video_exists(word):
                isl_sentence.append(capitalized_word)  # Use correct case
            else:
                spaced_word = " ".join(word.upper())  # Fingerspelling
                isl_sentence.append(spaced_word + "    ")

        isl_sequence.append(" ".join(isl_sentence))  # Combine ISL words for each sentence

    return " / ".join(isl_sequence)  # Separate sentences with '/'
