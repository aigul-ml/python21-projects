from abstract.serializers import BaseSerializer

from .models import User    # из этой же папки импортируем

class UserSerializer(BaseSerializer): # inherited from BaseSerializer
    class Meta: 
        fields = ['email', 'name', 'sex', 'is_authenticated']
        queryset = User.objects # переопределяем queryset
