from django.contrib import admin
from .models import Armor, WeaponTrait, Weapon, Gear, Price, Ammunition
# Register your models here.


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'group')
    list_filter = ('type', 'group')


class ArmorAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)

class AmmoAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Armor, ArmorAdmin)
admin.site.register(WeaponTrait)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Ammunition, AmmoAdmin)
admin.site.register(Gear)
admin.site.register(Price)