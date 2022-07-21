from abstract.serializers import BaseSerializer
from .models import Product, Comment


class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ("id", "category", "title", "price", "description", "comments")
        model = Product
    
class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ("id", "user", "body", "created_at")
        model = Comment

    def serialize_obj(self, obj):
        comment = super().serialize_obj(obj)
        comment["user"] = obj.user.username
        return comment