from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)

    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")

    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image

class CompressImage(models.Model):
    image = models.ImageField(upload_to='gallery')

    def save(self, *args, **kwargs):
        new_img = compress(self.image)
        self.image = new_img
        super().save(*args, **kwargs)