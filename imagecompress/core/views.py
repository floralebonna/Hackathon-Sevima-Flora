from django.shortcuts import render
from .forms import ImageForm
import os
#from .models import CompressImage

def compressView(request):
    img_up = None
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img_up = form.save()
    else:
        form=ImageForm()
    return render(request, 'index.html', {'form': form, 'img_up' :img_up})

def compresSize(request):
    img_up = None
    img_size = None
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img_up = form.save()
            img_path = img_up.image.path

            try:
                img_size = os.path.getsize(img_path)/1024
            except:
                img_size = None
    else:
        form=ImageForm()
    
    return render(request, 'index.html', {
        'form': form,
        'img_up' :img_up,
        'img_size': img_size
    })
