from django.contrib import admin

# Register your models here.

from models import Collision

class CollisionAdmin(admin.ModelAdmin):
    class Meta:
        model = Collision

admin.site.register(Collision, CollisionAdmin)
