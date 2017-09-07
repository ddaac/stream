from django.conf.urls import url

from .views import (
    DashboardView, ProfileView, ContentsView
)

urlpatterns = [
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^contents/$', ContentsView.as_view(), name='contents'),
]
