from django.shortcuts import render
import os
from django.conf import settings
from django.conf import settings
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


def gallery(request):
    # المسار الصحيح لمجلد gallery
    gallery_dir = os.path.join(settings.STATICFILES_DIRS[0], 'main', 'images', 'gallery')
    
    gallery_images = []
    
    if os.path.exists(gallery_dir):
        print(f"تم العثور على مجلد المعرض: {gallery_dir}")
        print(f"المحتويات: {os.listdir(gallery_dir)}")
        
        for filename in os.listdir(gallery_dir):
            file_path = os.path.join(gallery_dir, filename)
            if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # استخدم هذا المسار
                gallery_images.append(f'main/images/gallery/{filename}')
    
    print(f"الصور التي سيتم عرضها: {gallery_images}")
    return render(request, 'main/gallery.html', {'gallery_images': gallery_images})