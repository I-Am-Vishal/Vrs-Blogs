from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.
from . models import(BlogModel, Query)

# ------------------------------------------------------------------

class BlogModelAdmin(admin.ModelAdmin):
    list_display=('title',)
    # class Media:
    #     css = {
    #         "all": ("css/main.css",)
    #     }
    #     js = ("js/blog.js",)

# -------------------------------------------------------------------

admin.site.register(BlogModel,BlogModelAdmin)
admin.site.register(Query)


# -------------------------------------------------------------------

