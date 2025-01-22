from django.db import models

class ImageColor(models.Model):
    """
    Model to save images and the hex code for their center-most pixel(s)
    """
    upload_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    hex_code = models.CharField(max_length=7)

