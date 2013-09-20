# Create your views here.
from django.http import HttpResponse
from django.http import *
from django.utils.http import base36_to_int, is_safe_url
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import REDIRECT_FIELD_NAME,login as auth_login, logout as auth_logout, get_user_model
from django.contrib.sites.models import get_current_site
from django.template.response import TemplateResponse

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
                return HttpResponseRedirect('/user/password')
    return render_to_response('gestione_scuola/login.html', context_instance=RequestContext(request))


def logout(request, next_page=None,
           template_name='gestione_scuola/logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           current_app=None, extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)

    if redirect_field_name in request.REQUEST:
        next_page = request.REQUEST[redirect_field_name]
        # Security check -- don't allow redirection to a different host.
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path

    if next_page:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page)

    current_site = get_current_site(request)
    context = {
        'site': current_site,
        'site_name': current_site.name,
        'title': 'Scollegato'
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
        current_app=current_app)






@login_required(login_url='/login/')
def home(request):
    return HttpResponse("Project Home Implement")

@login_required(login_url='/login/')
def main(request):
    return HttpResponse("Main page")