from django.contrib import admin

from assets.models import Asset, AssetInWork


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(AssetInWork)
class AssetInWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset', 'worker', 'status', 'todo_date',
                    'begin_date', 'end_date', 'report')
    list_display_links = ('id', 'asset')
    list_editable = ('status',)
    list_filter = ('status', 'todo_date', 'begin_date', 'end_date')
