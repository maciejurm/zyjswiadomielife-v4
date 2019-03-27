from rest_framework import serializers
from .models import Embed

class EmbedSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Embed
        fields = '__all__'

