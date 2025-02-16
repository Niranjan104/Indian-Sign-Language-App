# Video/Audio/Text to Sign Language Converter

## Project Setup Guide

This guide will help you set up the Django backend for the **Video/Audio/Text to Sign Language Converter** web application.

### Prerequisites
Make sure you have the following installed:
- Python (>= 3.8)
- Virtual Environment (`venv`)
- pip (Python package manager)
- Django (latest version)
- FFmpeg (for audio/video processing)

---

## Step 1: Create a Virtual Environment
A virtual environment helps isolate dependencies for this project.

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

---

## Step 2: Install Django and Required Dependencies

Once the virtual environment is activated, install Django and other dependencies.

```bash
pip install --upgrade pip  # Upgrade pip to the latest version
pip install django djangorestframework pillow numpy opencv-python ffmpeg-python
```

If you have additional dependencies (e.g., TensorFlow, PyTorch, Speech-to-Text libraries), install them as well.

```bash
pip install tensorflow torchaudio speechrecognition transformers
```

---

## Step 3: Create a Django Project
Now, create a new Django project named `signlang_converter`.

```bash
django-admin startproject signlang_converter
cd signlang_converter
```

Run the server to verify the setup:

```bash
python manage.py runserver
```
If everything is correct, you should see the Django development server running at `http://127.0.0.1:8000/`.

---

## Step 4: Create a Django App
Create an app inside the project to handle video/audio/text processing.

```bash
python manage.py startapp converter
```

Add `converter` and required Django modules to `INSTALLED_APPS` in `signlang_converter/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'converter',  # Add the newly created app
]
```

---

## Step 5: Set Up Database Migrations
Run the following command to apply migrations:

```bash
python manage.py migrate
```

---

## Step 6: Create a Superuser (For Admin Access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

---

## Step 7: Install FFmpeg (For Audio/Video Processing)
FFmpeg is required for handling video and audio files.

- **Windows**: Download and install FFmpeg from [FFmpeg official website](https://ffmpeg.org/download.html)
- **Linux/macOS**:

```bash
sudo apt update && sudo apt install ffmpeg  # Debian/Ubuntu
brew install ffmpeg  # macOS
```

Check if FFmpeg is installed:

```bash
ffmpeg -version
```

---

## Step 8: Run the Server
Start the Django development server:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

## Step 9: Install Frontend Dependencies (Optional, if using React)
If you're integrating a React frontend, navigate to the frontend directory and install dependencies:

```bash
cd frontend
npm install
npm start
```

---

## Step 10: Create a `requirements.txt` File
To ensure that dependencies can be installed easily, generate a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

To install dependencies from the file:

```bash
pip install -r requirements.txt
```

---

## Additional Notes
- Use `python manage.py collectstatic` when deploying to production.
- Secure your `.env` file if using environment variables for API keys.
- Set up CORS and authentication for external API interactions.

---

## Next Steps
- Implement API endpoints for handling text/audio/video input.
- Integrate AI models for speech-to-text and video-to-sign-language conversion.
- Deploy the application using Docker or cloud services.

---

This completes the initial Django setup for the **Video/Audio/Text to Sign Language Converter** web application.
