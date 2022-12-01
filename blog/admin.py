from django.contrib import admin
from .models import Post, Category, Comment,  Contact, Subscribe


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at')
#    fields = ('title', 'desc')
#    readonly_fields = ('',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', "email")


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribe)