from django_filters import rest_framework as filters

from assets.models import Asset, AssetInWork


class AssetFilter(filters.FilterSet):
    """Фильтр поиска по активам."""
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Asset
        fields = ('name',)


class AssetInWorkFilter(filters.FilterSet):
    """Фильтр поиска по активам в работе."""
    status = filters.MultipleChoiceFilter(choices=AssetInWork.STATUS_CHOICES)
    todo_date = filters.DateTimeFromToRangeFilter(field_name='todo_date')
    begin_date = filters.DateTimeFromToRangeFilter(field_name='begin_date')
    end_date = filters.DateTimeFromToRangeFilter(field_name='end_date')

    class Meta:
        model = AssetInWork
        fields = ('status', 'todo_date', 'begin_date', 'end_date')
