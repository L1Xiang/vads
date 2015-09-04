from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    USER_TYPES = (('poster', 'Poster'), ('owner', 'ScreenOwner'))
    user = models.OneToOneField(User, related_name='user_profile', primary_key=True)
    user_type = models.CharField(max_length=10, null=True, choices=USER_TYPES)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank = False)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('vads:profile:detail', kwargs={'pk': self.pk})
    
#create a user profile object, when user signs up
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
def create_default_ad_list(sender, instance, created, **kwargs):
    if created:
        AdList.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
#post_save.connect(create_default_ad_list, sender=User)

class Screen(models.Model):
    user = models.ForeignKey(User, related_name='screens')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    class Meta:
        unique_together = ('user', 'name')
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Screen, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('vads:screen:detail', kwargs={'slug': self.slug})
    
    
# model classes for a ad
class AdList(models.Model):
    user = models.ForeignKey(User, related_name='ad_lists')
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=255, blank=False)
    info = models.TextField(max_length=1000, null=True)
    
    class Meta:
        unique_together = ('user', 'name')
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(AdList, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('vads:ad_lists:detail', kwargs={'slug': self.slug})
    
class Ad(models.Model):
    AD_TYPE = (('picture', 'Picture'), ('video', 'Video'))
    user = models.ForeignKey(User, related_name='ads', null=True)
    ad_list = models.ForeignKey(AdList, related_name='ads', null=True)
    name = models.CharField(max_length=255)
    ad_type = models.CharField(max_length = 10, null=True, choices=AD_TYPE)
    slug = models.SlugField(max_length=255)
    info = models.TextField(max_length=1000, null=True)

    class Meta:
        unique_together = ('user', 'name')
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ad, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('vads:ad:detail', kwargs={'slug': self.slug})
    
    
    

    
    
