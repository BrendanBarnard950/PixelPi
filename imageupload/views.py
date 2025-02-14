from django.shortcuts import render, redirect
from .models import ImageColor
from .model_forms import ImageUploadForm

def upload_image(request):
    """
    View to upload images. If upload is successful user is redirected to home page.
    """
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_images') 
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload_form.html', {'form': form})

def view_images(request):
    """
    View to render all existing images
    """
    images = ImageColor.objects.all().order_by('-upload_date')
    return render(request, 'image_list.html', {'images': images})

def delete_image(request, id):
    """
    This will delete a selected image
    """
    image = ImageColor.objects.get(pk=id)
    image.delete()
    return redirect('view_images')

def view_full_image(request, id):
    """
    This will display a full-size version of the image
    """
    image = ImageColor.objects.get(pk=id)
    return render(request, 'full_image.html', {'image': image})