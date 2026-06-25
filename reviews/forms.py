from django import forms
from .models import Review


# Review form
# Allows logged-in users to create and edit product reviews
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            'rating',
            'comment',
        ]

        labels = {
            'rating': 'Rating out of 5',
            'comment': 'Your Review',
        }