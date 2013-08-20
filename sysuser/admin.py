from django.contrib import admin
from sysuser.models import SysUser
from account.models import Account, AssignedPolicy
from allocation.models import Allocation


class AllocationInLine(admin.StackedInline):
    model=Allocation

class AccountInLine(admin.StackedInline):
    model = Account

class AssignPolicyInLine(admin.StackedInline):
    model = AssignedPolicy

class AccountAdmin(admin.ModelAdmin):
    inlines = [AssignPolicyInLine]

class SysUserAdmin(admin.ModelAdmin):
    inlines = [AccountInLine,AllocationInLine]


admin.site.register(SysUser, SysUserAdmin)
admin.site.register(Account,AccountAdmin)
