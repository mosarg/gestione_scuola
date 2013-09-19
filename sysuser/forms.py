from django import forms
from django.utils.datastructures import SortedDict
from account.models import Account
from backend.models import Backend
from .models import SysUser

class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set his/her password without entering the
    old password
    """
    error_messages = {
        'password_mismatch': "Errore: le due password non sono uguali",
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
    """
    A form that lets a user change his/her password by entering
    their old password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': "Vecchia password non corretta. "
                                "Inseriscila nuovamente",
    })
    old_password = forms.CharField(label="Old password",
                                   widget=forms.PasswordInput)

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'])
        return old_password

PasswordChangeForm.base_fields = SortedDict([
    (k, PasswordChangeForm.base_fields[k])
    for k in ['old_password', 'new_password1', 'new_password2']
])

