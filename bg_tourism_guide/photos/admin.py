from django.contrib import admin

from bg_tourism_guide.photos.models import Photo


class CustomPhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', 'uploaded_by', 'date_of_publication', 'location')
    list_filter = ('uploaded_by', 'date_of_publication', 'location')
    search_fields = ('uploaded_by', 'location', 'tagged_destinations')
    ordering = ('date_of_publication',)
    exclude = ('uploaded_by',)

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Photo, CustomPhotoAdmin)
