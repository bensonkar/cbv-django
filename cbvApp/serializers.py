from rest_framework import fields, serializers
from cbvApp.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=['id','name','score']