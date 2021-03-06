from django.contrib import admin
from .models import Writing, View, Message

class WritingAdmin(admin.ModelAdmin):
    list_display = ('title', 'num_views',)

    def num_views(self, instance):
        return instance.view_set.count()


class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('content', 'email',)


admin.site.register(Writing, WritingAdmin)
admin.site.register(View)
admin.site.register(Message, MessageAdmin)