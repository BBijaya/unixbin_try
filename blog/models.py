from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_save, post_delete
from django.dispatch import  receiver
from django.utils.text import slugify

# for random characters generation
import string
import random
# PIl for image resizing
from PIL import Image

# testing solr imagefield
from sorl.thumbnail import ImageField
# taggit
from taggit.managers import TaggableManager

# meta 
from meta.models import ModelMeta

from django.urls import reverse

# Create your models here.




def upload_location(instance, filename):
    """setting upload location for post media"""
    file_path = f"{instance.author.username}/{instance.title}-{filename}"
    return file_path

def random_string_generator(size=10):
    """
    random string generator
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

class PublishedManager(models.Manager):
    """
    filter post with status "published"
    """
    def get_queryset(self):
        """
        custom query to filter
        """
        published = super().get_queryset().filter(status='published')
        return published


class Post(ModelMeta, models.Model):
    """
    Post table for the blog
    """
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
    )

    CATEGORY_CHOICES = (
        ('uncategorized', 'UNCATEGORIZED'),
        ('debian', 'DEBIAN'),
        ('ubuntu', 'UBUNTU'),
        ('centos', 'CENTOS'),
        ('redhat', 'REDHAT'),
        ('archlinux', 'ARCHLINUX')
    )
    
    

    title = models.CharField(max_length=300, help_text="title of the post")
    slug = models.SlugField(max_length=300, unique=True, blank=True,   \
            help_text="seo friendly title for the post")

    thumbnail = models.ImageField(blank=False, null=False, upload_to=upload_location,\
                help_text="image for the thubnail fo the post (required)")

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="uncategorized")
    content = models.TextField(help_text="body of your post")
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", \
            help_text="select post author")

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft',\
        help_text="do you want to publish online or save it as draft")

    tags = TaggableManager()

    objects = models.Manager() # default manager of the model
    published = PublishedManager() # custom manager that return published item only

    _metadata = {
        'title': 'title',
        'description': 'content',
        'image': 'get_meta_image',
    }

    def get_meta_image(self):
        if self.thumbnail:
            return self.thumbnail.url 

    # def save(self, *args, **kwargs):
    #     """
    #     overriding default save for image resizing
    #     """
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.thumbnail.path)
    #     img.thumbnail((600, 500), Image.ANTIALIAS)
    #     img.save(self.thumbnail.path, quality=90)

    class Meta():
        """
        meta class
        """
        ordering = ['-date_created']
    
    def get_absolute_url(self):
        return reverse("post_detail",  args=[str(self.slug)])
    

    def __str__(self):
        """
        string representaion of the model
        """
        return str(self.title)

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    


@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, *args, **kwargs):
    instance.thumbnail.delete(False)

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    """
    if slug is not generated , generate the slug adding 10 random chars before title
    """
    if not instance.slug:
        # instance.slug = slugify(random_string_generator(size=8) +"/"+ instance.title)
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_post_receiver, sender=Post)



class Email(ModelMeta, models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        """
        meta class
        """
        ordering = ['-date_added']

    def __str__(self):
        return str(self.email)


