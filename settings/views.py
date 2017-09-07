from django.views import View
from django.shortcuts import render


class DashboardView(View):
    def get(self, request, *arg, **kwargs):
        context = {}
        return render(request, 'settings/dashboard/index.html', context)


class ProfileView(View):
    def get(self, request, *arg, **kwargs):
        context = {}
        return render(request, 'settings/profile/index.html', context)


class ContentsView(View):
    def get(self, request, *arg, **kwargs):
        context = {}
        return render(request, 'settings/contents/index.html', context)
