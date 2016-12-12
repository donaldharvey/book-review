from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import BookReviewForm
from .models import BookReview

# Create your views here.
def index(request):
	return render(request, "first_app/index.html")

def registration(request):
	return render(request, "first_app/registration.html")

def login(request):
	return render(request, "first_app/login.html")

@login_required
def reviews(request):
	return render(request, "first_app/reviews.html")

@login_required
def review(request, review_id):
    review = get_object_or_404(BookReview, id=review_id)

    return render(request, "first_app/review.html", {'review': review})

@login_required
def edit_review(request, review_id=None):
    review = None

    if review_id is not None:
        review = get_object_or_404(BookReview, id=review_id)

    form = BookReviewForm(instance=review)

    if request.method == 'POST':
        form = BookReviewForm(request.POST, instance=review)

        if form.is_valid():
            # form.instance = BookReview([form_parameters]) 
            book_review = form.instance
            book_review.author = request.user
            book_review.save()
            return HttpResponseRedirect(book_review.get_absolute_url())

    return render(request, "first_app/create_review.html", {'form': form, 'review': review})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(BookReview, id=review_id)
    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect('/reviews/')
        
    return render(request, "first_app/delete_review.html", {'review': review})

def comments(request):
	return render(request, "first_app/comments.html")
