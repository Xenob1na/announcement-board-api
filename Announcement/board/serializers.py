from rest_framework.serializers import ModelSerializer

from .models import Announcement, Category

class BoardSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = ["id", "title", "description", "price", "image"]
        
class BoardDetailSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = ["id", "title", "description", "body", "price", "image", "location", "created_at", "created_by"]