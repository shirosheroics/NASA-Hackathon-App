from django.contrib import admin
from .models import (Article, Camp, Hazerd,
 Maped, Material, Profile, Quest, Task)

# Register your models here.
admin.site.register(Article)
admin.site.register(Camp)
admin.site.register(Hazerd)
admin.site.register(Maped)
admin.site.register(Material)
admin.site.register(Profile)
admin.site.register(Quest)
admin.site.register(Task)
