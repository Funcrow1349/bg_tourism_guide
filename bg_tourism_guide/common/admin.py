from django.contrib import admin
from bg_tourism_guide.common.models import Comment


class CustomCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'comment_author', 'to_photo', 'date_time_of_publication')
    list_filter = ('comment_author', 'date_time_of_publication')
    search_fields = ('comment_author', 'to_photo',)
    ordering = ('date_time_of_publication',)
    exclude = ('comment_author',)

    def save_model(self, request, obj, form, change):
        if not obj.comment_author:
            obj.comment_author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Comment, CustomCommentAdmin)
