from rest_framework import serializers
from .models import Project, Issue, Tag, User, Team, BugTag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')




class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')

class BugTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugTag
        fields = ('__all__')



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

    
class IssueSerializer(serializers.ModelSerializer):
        class Meta:
            model = Issue
            fields = ('__all__')
