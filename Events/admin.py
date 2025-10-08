from django.contrib import admin
from django import forms
from .models import Event, CouncilEventParticipation


class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "speakers": forms.Textarea(attrs={"rows": 3, "cols": 50}),
            "partners": forms.Textarea(attrs={"rows": 3, "cols": 50}),
        }

class CouncilEventParticipationInline(admin.TabularInline):
    model = CouncilEventParticipation
    extra = 1
    autocomplete_fields = ("council_member",)
    fields = ("council_member", "role_in_event", "attended")
    show_change_link = True

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

    list_display = (
        'title', 'location', 'time', 'end_time', 'status',
        'registration_required', 'capacity'
    )
    search_fields = ('title', 'location', 'description')
    list_filter = ('status', 'location', 'registration_required')
    ordering = ('-time',)

    fieldsets = (
        ("Event Info", {"fields": ("title", "description", "location")}),
        ("Timing", {"fields": ("time", "end_time")}),
        ("Details", {"fields": ("speakers", "partners", "capacity")}),
        ("Registration & Status", {"fields": ("status", "registration_required", "registration_link")}),
        ("System Info", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    readonly_fields = ('created_at', 'updated_at')
    inlines = [CouncilEventParticipationInline]

@admin.register(CouncilEventParticipation)
class CouncilEventParticipationAdmin(admin.ModelAdmin):
    list_display = ("event", "council_member", "role_in_event", "attended")
    search_fields = (
        "event__title",
        "council_member__student__first_name",
        "council_member__student__last_name"
    )
    list_filter = ("attended", "role_in_event")
