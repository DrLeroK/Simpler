from django.db import models
# Provides Django's model infrastructure for database interactions
from django.urls import reverse
# Used for URL reversing (generating URLs from view names)
from django.utils.text import slugify
# Converts strings to URL-friendly slugs (e.g., "My Group" → "my-group")
import markdown
# Markdown processing library (converts markdown to HTML)
from django.contrib.auth import get_user_model
# Gets the currently active User model (custom or default)
from django.conf import settings
# Provides access to Django settings


User = get_user_model()
#  Stores reference to the active User model for use in relationships


# Create your models here.
class Group(models.Model):  # Has many-to-many relationship with Users through GroupMember
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    # URL-friendly version of name
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, blank=True, default='')
    # Stores HTML version of description
    members = models.ManyToManyField(User, through='GroupMember', related_name='group_members')
    # Many-to-many with User via GroupMember
    # through='GroupMember': Specifies the intermediate model that will manage the relationship
    # related_name='group_members': Defines the reverse relation name from User back to Group
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_groups', default=None)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = markdown.markdown(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})
    
     # Add these new methods here:
    def get_member_count(self):
        """Returns the number of members in this group"""
        return self.membership.count()
        
    def get_post_count(self):
        """Returns the number of posts in this group"""
        return self.posts.count()
    
    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_groups')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='membership') 

    def __str__(self):
        return f"{self.user.username} in {self.group.name}" 
    
    class Meta:
        unique_together = ('user', 'group')

