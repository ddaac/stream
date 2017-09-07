from django.views import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *arg, **kwargs):
        return render(request, 'dashboard/index.html')
