from django.views import View
from django.shortcuts import render


class UserReviewsView(View):
    def get(self, request, *arg, **kwargs):
        username = kwargs.get('username', 0)
        context = {}
        return render(request, 'account/reviews/index.html', context)


class UserContentsView(View):
    def get(self, request, *arg, **kwargs):
        context = {}
        return render(request, 'account/contents/index.html', context)


class UserContentsviewView(View):
    def get(self, request, *arg, **kwargs):
        context = {}
        return render(request, 'account/contents/view.html', context)


class UserInfoView(View):
    def get(self, request, *arg, **kwargs):
        context = {}
        return render(request, 'account/info/index.html', context)
