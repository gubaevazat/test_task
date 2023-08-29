from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import serializers
from rest_framework.serializers import ValidationError
from djoser import serializers as djoser_serializers
from drf_spectacular.utils import extend_schema_field

from assets.models import Asset, AssetInWork

User = get_user_model()


class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)
        model = Asset


class AssetInWorkSerializerGet(serializers.ModelSerializer):
    worker = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    asset = serializers.StringRelatedField()

    class Meta:
        model = AssetInWork
        fields = ('id', 'asset', 'worker', 'status', 'todo_date',
                  'begin_date', 'end_date', 'report')


class AssetInWorkSerializerPost(serializers.ModelSerializer):
    asset = serializers.PrimaryKeyRelatedField(
        queryset=Asset.objects.all()
    )
    status = serializers.ChoiceField(
        choices=AssetInWork.STATUS_CHOICES,
        required=True
    )
    worker = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AssetInWork
        fields = ('asset', 'worker', 'status', 'report')

    def validate(self, data):
        if data['status'] == 'CO':
            return data
        if AssetInWork.objects.filter(
            Q(asset=data['asset']),
            Q(status=data['status']),
        ).exists():
            raise ValidationError(
                'Актив уже в работе или размещён в листе ожидания!'
            )
        return data

    def to_representation(self, instance):
        return AssetInWorkSerializerGet(instance, context=self.context).data


class CustomUserSerializer(djoser_serializers.UserSerializer):

    assets_in_work = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'assets_in_work')
        read_only_fields = ('id', 'assets_in_work')

    @extend_schema_field(AssetInWorkSerializerGet(many=True))
    def get_assets_in_work(self, obj):
        assets = list(AssetInWork.objects.filter(
            worker=obj).values())
        return AssetInWorkSerializerGet(assets, many=True).data
