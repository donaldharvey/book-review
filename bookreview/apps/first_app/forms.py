from django import forms
from .models import BookReview

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['book', 'content', 'title']
        widgets = {
            'book': forms.RadioSelect
        }