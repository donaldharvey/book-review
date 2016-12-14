from django import forms
from .models import BookReview

class BookReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[
        (1,"1 star"),
        (2,"2 stars"),
        (3,"3 stars"),
        (4,"4 stars"),
        (5,"FIVE STARS!")
    ], initial=3)

    class Meta:
        model = BookReview
        fields = ['book', 'content', 'title', 'rating']
        widgets = {
            'book': forms.RadioSelect
        }