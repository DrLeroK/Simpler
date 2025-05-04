from django.db import IntegrityError
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages 
from django.urls import reverse_lazy
from groups.models import Group, GroupMember
from . import models


# Create your views here.
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class SingleGroup(generic.DetailView):  # Keeping your original class name
    model = Group
    template_name = 'groups/group_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.get_object()
        
        if self.request.user.is_authenticated:
            # Using the related_name='user_groups' from GroupMember model
            context['user_groups'] = self.request.user.user_groups.select_related('group')
            
            # Get groups the user isn't a member of
            context['other_groups'] = Group.objects.exclude(
                members=self.request.user
            ).distinct()
        else:
            # For anonymous users, show all groups
            context['other_groups'] = Group.objects.all()
        
        # Get posts for this group with related user data
        context['post_list'] = group.posts.select_related('user', 'group').all()
        return context


class ListGroups(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Warning already a member')
        else: 
            messages.success(self.request, 'you are now a member')

        return super().get(request, *args, **kwargs)
        # Executes the redirect after processing.
    

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, 'sorry you are not in this group')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group')
        return super().get(request, *args, **kwargs)


class DeleteGroup(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Group
    template_name = 'groups/group_confirm_delete.html'
    success_url = reverse_lazy('groups:all')

    def test_func(self):
        group = self.get_object()
        return self.request.user == group.creator or self.request.user.is_superuser
