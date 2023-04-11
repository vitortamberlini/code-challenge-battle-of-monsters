from django.contrib import admin

# Register your models here.
from battle.models import Battle

admin.site.register(Battle)

admin.site.site_title = "Battle - Administration"
admin.site.site_header = "Battle - Administration"
