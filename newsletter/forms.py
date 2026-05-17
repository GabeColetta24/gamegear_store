from django import forms
from .models import NewsletterSignup


# Newsletter signup form
# Allows users to join the mailing list
class NewsletterSignupForm(forms.ModelForm):

    class Meta:
        model = NewsletterSignup
        fields = [
            'email',
        ]