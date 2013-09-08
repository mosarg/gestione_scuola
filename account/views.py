from account.forms import PasswordForm
from django.views.generic.edit import FormView

class PasswordChangeView(FormView):
    template_name = 'account/passwd.html'
    form_class = PasswordForm
    success_url = '/thanks/'
    def form_valid(self, form):

        return super(PasswordChangeView, self).form_valid(form)
