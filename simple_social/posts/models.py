from django.db import models
from django.conf import settings
from django.urls import reverse
import markdown
from groups.models import Group
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    # ForeignKey to User model
    # related_name='posts': User.posts accesses all their posts
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        self.message_html = markdown.markdown(self.message)
        super().save(*args, **kwargs)
        # Calls parent class save()

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={
            'username': self.user.username,  # Access via the user ForeignKey
            'pk': self.pk
        })
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']











