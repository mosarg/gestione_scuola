# Create your views here.
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import SysUser
from account.models import Account
from backend.models import Backend
from django.utils import timezone
from braces.views import LoginRequiredMixin
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse("Hello, world. You're at the sysuser index.")


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

