from django.contrib import admin
from .models import website,FormData,Document

# Register your models here.
admin.site.register(website)

admin.site.register(FormData)

admin.site.register(Document)