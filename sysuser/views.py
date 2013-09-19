# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import SysUser
from account.models import Account
from backend.models import Backend
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from sysuser.forms import PasswordChangeForm


from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse("Hello, world. You're at the sysuser index.")


@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='sysuser/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('sysuser.views.password_change_done')
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)



@login_required
def password_change_done(request,
                         template_name='sysuser/password_change_done.html',
                         current_app=None, extra_context=None):
    context = {}
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)
















class SysuserDetailView(LoginRequiredMixin,DetailView):
    model=SysUser
    template_name = 'sysuser/sysuser-detail.html'

    # def get_queryset(self):
    #     currentUser = User.objects.get(username = self.request.user)
    #     djangoBackend=Backend.objects.get(kind='django')
    #     uidNumber=currentUser.id
    #     systemAccount=Account.objects.filter(backendId=djangoBackend.backendId).get(backendUidNumber=currentUser.id)
    #     self.kwargs.set('pk')=14
    #     return SysUser.objects.filter(pk=systemAccount.userId.pk)

    def get_object(self):
        currentUser = User.objects.get(username = self.request.user)
        djangoBackend=Backend.objects.get(kind='django')
        uidNumber=currentUser.id
        systemAccount=Account.objects.filter(backendId=djangoBackend.backendId).get(backendUidNumber=currentUser.id)
        return  get_object_or_404(SysUser,pk=systemAccount.userId.pk)

    # def get_context_data(self, **kwargs):
    #     context = super(SysuserDetailView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

