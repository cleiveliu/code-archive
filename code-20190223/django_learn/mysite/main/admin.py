from django.contrib import admin

# Register your models here.
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    fields = [
        "tutorial_title",
        "tutorial_pulished",
        "tutorial+content"
    ]


admin.site.register(Tutorial, TutorialAdmin)
