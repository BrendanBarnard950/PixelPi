from django.forms import ModelForm
from .models import ImageColor

from PIL import Image, UnidentifiedImageError

class ImageUploadForm(ModelForm):
    class Meta:
        model = ImageColor
        fields = ['image']
        # Making the label blank so I can make a custom one on the template
        labels = {
            'image': ''
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
    
    def extractCenterColour(self, image_to_process):
        """
        This method extracts the colour of the centermost pixel of an image, or the average of the center group
        of pixels if one or both of the dimensions of the image are even
        """
        try:
            with Image.open(image_to_process) as image:
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                width, height = image.size

                # Determine the central region of the image
                horizontal_center = width // 2
                vertical_center = height // 2

                if width % 2 == 1 and height % 2 == 1:  # Single center pixel
                    center_pixel = image.getpixel((horizontal_center, vertical_center))
                    hex_code = '#{:02x}{:02x}{:02x}'.format(*center_pixel)
                else:
                    # Determine the region for even dimensions
                    center_region_left_edge = horizontal_center - (1 if width % 2 == 0 else 0)
                    center_region_upper_edge = vertical_center - (1 if height % 2 == 0 else 0)
                    center_region_right_edge = horizontal_center + 1
                    center_region_lower_edge = vertical_center + 1

                    cropped_region = image.crop((center_region_left_edge, center_region_upper_edge, center_region_right_edge, center_region_lower_edge))
                    center_pixels = list(cropped_region.getdata())
                    average_color = tuple(sum(channel) // len(center_pixels) for channel in zip(*center_pixels))
                    hex_code = '#{:02x}{:02x}{:02x}'.format(*average_color)

            return hex_code
        except Exception as exc:
            raise ValidationError(f'An error occurred while processing the image: {str(exc)}')
    
    def clean_image(self):
        """
        This method checks if the file is an image by trying to open it with PIL. It is more resource-heavy than just checking
        the file extension, but will protect against intentional mislabelig.
        """
        image = self.cleaned_data.get('image')  # Get the uploaded image file
        if not image:
            raise ValidationError('No file was uploaded.')

        try:
            with Image.open(image) as img:
                img.verify()  # Verify the integrity of the image
        except UnidentifiedImageError:
            raise ValidationError('The file you uploaded is not a valid image.')
        except Exception as e:
            raise ValidationError(f'An error occurred while processing the image: {str(e)}')

        return image
        
    def save(self):
        hex = self.extractCenterColour(self.cleaned_data['image'])
        self.instance.hex_code = hex
        super().save()    
    