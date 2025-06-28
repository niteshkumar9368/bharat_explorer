from django.contrib import admin
from .models import State, TouristPlace, PlaceImage, Category
from django.utils.html import format_html

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(State, StateAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    readonly_fields = ('image_tag',)
    fields = ('image_tag', 'image')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return ""
    image_tag.short_description = 'Image Preview'

class TouristPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'category', 'description', 'best_time', 'location')
    search_fields = ('name', 'state__name')
    exclude = ('main_image_url',)
    inlines = [PlaceImageInline]

admin.site.register(TouristPlace, TouristPlaceAdmin)
admin.site.register(PlaceImage)
