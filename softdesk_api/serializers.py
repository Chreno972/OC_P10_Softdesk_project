from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User, Contributors, Projects, Issues, Comments


class UserListSerializer(ModelSerializer):
    """_summary_

    Args:
        ModelSerializer (_type_): _description_
    """
    class Meta:
        """_summary_
        """
        model = User
        fields = ['id', 'first_name']


class UserDetailSerializer(ModelSerializer):
    """_summary_

    Args:
        ModelSerializer (_type_): _description_
    """
    users = SerializerMethodField()

    class Meta:
        """_summary_
        """
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']


class ContributorListSerializer(ModelSerializer):
    """_summary_"""
    class Meta:
        """_summary_"""
        model = Contributors
        fields = ['id', 'project', 'user']


class ContributorDetailSerializer(ModelSerializer):
    """_summary_

    Args:
        ModelSerializer (_type_): _description_
    """
    contributors = SerializerMethodField()

    class Meta:
        """_summary_"""
        model = Contributors
        fields = ['id', 'project', 'user', 'permission', 'role']


class ProjectListSerializer(ModelSerializer):
    """_summary_"""
    class Meta:
        """_summary_"""
        model = Projects
        fields = ['id', 'title', 'type', 'author']


class ProjectDetailSerializer(ModelSerializer):
    """_summary_

    Args:
        ModelSerializer (_type_): _description_
    """
    contributors = SerializerMethodField()

    class Meta:
        """_summary_"""
        model = Projects
        fields = [
            'id',
            'title',
            'description',
            'type',
            'author',
            'contributors',
        ]


class IssueListSerializer(ModelSerializer):
    """_summary_"""
    class Meta:
        """_summary_"""
        model = Issues
        fields = [
            'id'
            'title',
            'author',
            'priority',
            'status',
            'date_created'
        ]


class IssueDetailSerializer(ModelSerializer):
    """_summary_"""
    contributors = SerializerMethodField()

    class Meta:
        """_summary_"""
        model = Issues
        fields = [
            'id',
            'title',
            'description',
            'tag',
            'priority',
            'status',
            'author',
            'date_created',
            'contributors',
        ]


class CommentListSerializer(ModelSerializer):
    """_summary_"""
    class Meta:
        """_summary_
        """
        model = Comments
        fields = ['id', 'author_user_id', 'date_created']


class CommentDetailSerializer(ModelSerializer):
    """_summary_

    Args:
        ModelSerializer (_type_): _description_
    """
    comments = SerializerMethodField()

    class Meta:
        """_summary_"""
        model = Comments
        fields = [
            'id',
            'description',
            'author_user_id',
            'issue_id',
            'date_created',
        ]
