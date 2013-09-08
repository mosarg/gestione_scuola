# Create your views here.
from django.http import HttpResponse


from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user/account')
    return render_to_response('gestione_scuola/login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')


def home(request):
    return HttpResponse("Project Home Implement")
def main(request):
    return HttpResponse("Main page")