from .models import App
from rest_framework import serializers
class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ['app_name','app_link','icon_link','category','sub_category','points']