from django.utils import timezone
from datetime import timedelta
from django.views.generic import TemplateView
from posts.models import Post
from groups.models import Group

class SuccessPage(TemplateView):
    template_name = "success.html"  # Make sure this matches your template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            # Get groups the user hasn't joined
            context['unjoined_groups'] = Group.objects.exclude(
                members=self.request.user
            )
            
            # Get recent posts from last 24 hours
            context['recent_posts'] = Post.objects.filter(
                created_at__gte=timezone.now() - timedelta(days=1)
            ).select_related('user', 'group')
        
        return context

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
    

class HomePage(TemplateView):
    template_name = 'index.html'

    