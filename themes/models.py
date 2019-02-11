from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator
from market import settings

def thumbnail_upload_path(instance, filename):
    return f'images/{instance.theme.id}/thumbnail/{filename}'

def screenshot_upload_path(instance, filename):
    return f'images/{instance.theme.id}/screenshot/{filename}'

def theme_file_upload_path(instance, filename):
    return f'download/{instance.id}/{instance.name}/{filename}'


class UserDownloadLog(models.Model):
    """user download log
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey('themes.Theme', on_delete=models.CASCADE)
    download_times = models.IntegerField(default=0)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user, self.theme, self.download_times}'


class Theme(models.Model):
    """themes
    """
    BS_V3 = '3'
    BS_V4 = '4'

    BOOTSTRAP_CHOICES = (
        (BS_V3, 'Bootstrap 3.x'),
        (BS_V4, 'Bootstrap 4.x'),
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5)])
    price = models.FloatField()
    discount = models.FloatField(blank=True,null=True)
    version = models.CharField(max_length=50, default="0.0.0.0")
    bootstrap = models.CharField(max_length=50, choices=BOOTSTRAP_CHOICES, default=BS_V3)
    browser = models.ManyToManyField('themes.Browser', blank=True)
    uses_less = models.BooleanField()
    uses_sass = models.BooleanField()
    category = models.ForeignKey('themes.Category', on_delete=models.CASCADE, blank=True)
    topic = models.ForeignKey('themes.Topic', on_delete=models.CASCADE, blank=True)
    labels = models.ManyToManyField('themes.Label', blank=True)
    license = models.ForeignKey('themes.License', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to=theme_file_upload_path, null=True)
    
    release_date = models.DateField(auto_now=False,auto_now_add=False, blank=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name, self.price, self.rating, self.version, self.file}'

    
class Review(models.Model):
    """review
    """
    theme = models.ForeignKey('themes.Theme', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.theme, self.user, self.rating, self.comment,}'


class Screenshot(models.Model):
    """screenshot
    """
    theme = models.ForeignKey('themes.Theme', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=screenshot_upload_path)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.theme, self.image,}'


class Thumbnail(models.Model):
    """thumbnail
    """
    theme = models.ForeignKey('themes.Theme', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_path)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.theme, self.thumbnail,}'


class Browser(models.Model):
    """browsers
    """
    browser = models.CharField(max_length=100)
    
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.browser,}'


class Category(models.Model):
    """category
    """
    category = models.CharField(max_length=100)
    
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.category,}'


class Topic(models.Model):
    """topic
    """
    topic = models.CharField(max_length=100)
    
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.topic,}'


class Label(models.Model):
    """lable
    """
    label = models.CharField(max_length=50)
    
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.label,}'


class License(models.Model):
    """license
    """
    license = models.CharField(max_length=100)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.license,}'




