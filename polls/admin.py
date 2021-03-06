from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

from django.contrib import admin

from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)
