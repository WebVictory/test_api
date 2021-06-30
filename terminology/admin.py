from django.contrib import admin
from terminology.models import Directory, Element

class DirectoryAdmin(admin.ModelAdmin):
    pass

class ElementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Element, ElementAdmin)
admin.site.register(Directory, DirectoryAdmin)