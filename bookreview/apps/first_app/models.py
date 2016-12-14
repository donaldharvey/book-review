from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Book(models.Model):
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	summary = models.TextField()
	image = models.ImageField(blank=True, null=True, upload_to="uploads/books/thumbnails/") #is this the correct way to store images in the database and is it recommended
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

class BookReview(models.Model):
	author = models.ForeignKey('auth.User', related_name='reviews')

	book = models.ForeignKey('Book', related_name='reviews')
	title = models.CharField(max_length=100)
	content = models.TextField() # TODO: use markdown here :)

	rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

	creation_time = models.DateTimeField(auto_now_add=True)
	last_edit_time = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('review', args=(self.id,))

class Comment(models.Model):
	author = models.ForeignKey('auth.User', related_name='comments')
	review = models.ForeignKey('BookReview', related_name='comments')
	timestamp = models.DateTimeField(auto_now_add=True)	
	text = models.TextField()
