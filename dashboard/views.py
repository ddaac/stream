from django.views import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *arg, **kwargs):
        context = {}
        return render(request, 'dashboard/index.html', context)
