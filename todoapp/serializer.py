from rest_framework import serializers
from todoapp.models import Todos

class TodoSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    completed_status=serializers.CharField(read_only=False)
    class Meta:
        model=Todos

        fields=["id",
                "task_name",
                "user",
                "completed_status"]