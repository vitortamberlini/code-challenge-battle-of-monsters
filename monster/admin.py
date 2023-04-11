from django.contrib import admin

# Register your models here.
from monster.models import Monster

admin.site.register(Monster)

admin.site.site_title = "Monster - Administration"
admin.site.site_header = "Monster - Administration"
