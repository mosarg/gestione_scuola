from django.contrib import admin
from account.models import Policy
from group.models import Group,  GroupPolicy

class GroupPolicyInline(admin.StackedInline):
    model=GroupPolicy



class PolicyAdmin(admin.ModelAdmin):
    inlines = [GroupPolicyInline]


admin.site.register(Policy,PolicyAdmin)