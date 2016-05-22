from django.contrib import admin
from .models import Writing, View

class WritingAdmin(admin.ModelAdmin):
    list_display = ('title', 'num_views',)

    def num_views(self, instance):
        return instance.view_set.count()

admin.site.register(Writing, WritingAdmin)
admin.site.register(View)
