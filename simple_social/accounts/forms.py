from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        # Uses whatever User model is active in settings, flexiable
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Fields:", self.fields.keys())
        self.fields["username"].label = "Username"
        self.fields['username'].help_text = '150 characters or fewer'
        self.fields["email"].label = "Email Address"
        self.fields["password1"].label = "Password"
        self.fields['password1'].help_text = 'At least 8 characters'
        self.fields["password2"].label = "Confirm Password"

    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use")
        return email
