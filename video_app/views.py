from video_app.utils.audio_to_text import audio_to_text
from video_app.utils.isl_video_matcher import find_best_match
from video_app.utils.text_to_isl import convert_to_isl
from video_app.utils.trie import Trie
from video_app.utils.video_to_text import video_to_text
import os
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
import json

def index(request):
    return render(request, 'video_app/converter.html')

MEDIA_DIR = settings.MEDIA_ROOT
isl_trie = Trie()
def process_media(request):
    isl_video_paths = []
    extracted_text = ""
    uploaded_video_path = None

    if request.method == 'POST':
        if request.FILES.get('video'):
            file = request.FILES['video']
            uploaded_video_path = default_storage.save(f'media/{file.name}', file)
            extracted_text = video_to_text(os.path.join(MEDIA_DIR, uploaded_video_path))
        elif request.FILES.get('audio'):
            file = request.FILES['audio']
            file_path = default_storage.save(f'media/{file.name}', file)
            extracted_text = audio_to_text(os.path.join(MEDIA_DIR, file_path))

        elif request.POST.get('text'):
            extracted_text = request.POST.get('text')

        else:
            return JsonResponse({'error': 'No valid media uploaded'}, status=400)

        isl_text = convert_to_isl(extracted_text)
        words = isl_text.split()
        for word in words:
            video_file_path = os.path.join(MEDIA_DIR, f"{word}.mp4")
            if os.path.exists(video_file_path):
                isl_video_paths.append(f"/media/{word}.mp4")
            else:
                best_match = find_best_match(word)
                if best_match:
                    isl_video_paths.append(f"/media/{best_match}.mp4")

        return render(request, 'video_app/converter.html', {
            'transcribed_text': extracted_text,
            'isl_text': isl_text,
            'video_paths': json.dumps(isl_video_paths),
            'uploaded_video': f"/media/{uploaded_video_path}" if uploaded_video_path else None
        })

    return render(request, 'video_app/converter.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'video_app/contact_us.html', {'form': form})

def about_us(request):
    return render(request, 'video_app/about_us.html')

def privacy_policy(request):
    return render(request, 'video_app/privacy_policy.html')