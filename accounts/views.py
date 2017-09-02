from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from accounts.models import User


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.request.user.id)
        return context
