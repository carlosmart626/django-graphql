from django.contrib import admin

from .models import HumanCharacter, DroidCharacter


class HumanCharacterAdmin(admin.ModelAdmin):
    pass


class DroidCharacterAdmin(admin.ModelAdmin):
    pass


admin.site.register(HumanCharacter, HumanCharacterAdmin)
admin.site.register(DroidCharacter, DroidCharacterAdmin)
