from django.contrib import admin
from wishapp.models import Dreamer, Desire

class DreamerInline(admin.StackedInline):
    model = Desire
    extra = 1

class DreamerAdmin(admin.ModelAdmin):
    fields = ['dreamer_name']
    inlines = [DreamerInline]


admin.site.register(Dreamer, DreamerAdmin)
# Register your models here.
