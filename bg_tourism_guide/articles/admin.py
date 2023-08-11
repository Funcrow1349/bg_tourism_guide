from django.contrib import admin
from bg_tourism_guide.articles.models import Article


class CustomArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    list_filter = ('author', 'created')
    search_fields = ('title', 'author', 'tagged_destinations')
    ordering = ('created',)
    exclude = ('author',)

    # set the author automatically upon creation from the admin page
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, CustomArticleAdmin)
