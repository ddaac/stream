from django.conf.urls import url

from .views import (
    UserContentsView, UserContentsviewView, UserInfoView, UserReviewsView
)

urlpatterns = [
    url(r'^contents/$', UserContentsView.as_view(), name='contents'),
    url(r'^contents/view/$', UserContentsviewView.as_view(), name='contentsview'),
    url(r'^info/$', UserInfoView.as_view(), name='info'),
    url(r'^reviews/$', UserReviewsView.as_view(), name='reviews'),
]
