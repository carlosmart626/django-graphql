from django.contrib import admin

from .models import HumanCharacter, DroidCharacter


class HumanCharacterAdmin(admin.ModelAdmin):
    filter_horizontal = ('friends', 'appears_in')


class DroidCharacterAdmin(admin.ModelAdmin):
    filter_horizontal = ('appears_in', )


admin.site.register(HumanCharacter, HumanCharacterAdmin)
admin.site.register(DroidCharacter, DroidCharacterAdmin)
