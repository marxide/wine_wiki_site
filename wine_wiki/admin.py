from django.contrib import admin
from .models import Wine, Producer, Variety

admin.site.register(Wine)
admin.site.register(Producer)
admin.site.register(Variety)
