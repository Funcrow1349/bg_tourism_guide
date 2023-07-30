from django.contrib import admin

from bg_tourism_guide.destinations.models import Destination


class CustomDestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'author', 'created')
    list_filter = ('type', 'author', 'created')
    search_fields = ('name', 'author', 'type')
    ordering = ('created',)
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Destination, CustomDestinationAdmin)
