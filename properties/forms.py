from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']
        widgets = {
            'review_text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your review...',
                'class': 'form-control'
            }),
        }
        labels = {
            'review_text': 'Your review'
        }