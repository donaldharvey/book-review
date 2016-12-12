from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'), #url expression where 127.0.0.1:8000/index leads to website
	# url(r'^login/$', views.login, name='login'), #url expression where 127.0.0.1:8000/login leads to website
	url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^reviews/(?P<review_id>\d+)/$', views.review, name='review'),
    url(r'^reviews/(?P<review_id>\d+)/delete/$', views.delete_review, name='delete_review'),
    
    url(r'^reviews/create/$', views.edit_review, name='create_review'),
    url(r'^reviews/(?P<review_id>\d+)/edit/$', views.edit_review, name='edit_review'),

    # url(r'^reviews/(?P<review_id>\d+))/comment/$', views.add_comment, name='add_comment'),
    # url(r'^reviews/(?P<review_id>\d+))/comment/delete/$', views.delete_comment, name='add_comment'),

	# url(r'^registration/$', views.registration, name='registration'), 
	url(r'^comments/$', views.comments, name='comments'),
]