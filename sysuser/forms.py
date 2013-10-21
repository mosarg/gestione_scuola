from django import forms
from django.utils.datastructures import SortedDict
from account.models import Account
from backend.models import Backend
from .models import SysUser

class SetPasswordForm(forms.Form):

    error_messages = {
        'password_mismatch': "Errore: le due password non sono uguali",
        'password_to_short': "Errore: lunghezza minima password 6 caratteri"
    }
    new_password1 = forms.CharField(label="New password",
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="New password confirmation",
                                    widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'])
            if len(password1)<6:
                raise forms.ValidationError(
                    self.error_messages['password_to_short'])
        return password2

    def save(self, commit=True):

        djangoBackend = Backend.objects.get(kind='django')
        uidNumber = self.user.id
        systemAccount= Account.objects.filter(backendId=djangoBackend.backendId).get(backendUidNumber=uidNumber)
        systemUser = SysUser.objects.get( pk=systemAccount.userId.pk)

        if commit:
            for account in systemUser.accounts.all():
                account.changeBackendPassword(self.cleaned_data['new_password1'])
        return self.user


class PasswordChangeForm(SetPasswordForm):

    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': "Vecchia password non corretta. "
                                "Inseriscila nuovamente",
    })
    old_password = forms.CharField(label="Old password",
                                   widget=forms.PasswordInput)

    def clean_old_password(self):

        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'])
        return old_password

PasswordChangeForm.base_fields = SortedDict([
    (k, PasswordChangeForm.base_fields[k])
    for k in ['old_password', 'new_password1', 'new_password2']
])

