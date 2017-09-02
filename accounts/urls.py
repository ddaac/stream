from django.conf.urls import url

from accounts.views import UserProfileView

urlpatterns = [
    url(r'^accounts/profile/$', UserProfileView.as_view(), name='user_detail'),
]
