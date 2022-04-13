# from django.shortcuts import render

# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from rest_framework.permissions import IsAuthenticated 
from .models import (
    User,
    Contributors,
    Projects,
    Issues,
    Comments,
)
from .serializers import (
    UserListSerializer,
    UserDetailSerializer,
    ContributorListSerializer,
    ContributorDetailSerializer,
    ProjectListSerializer,
    ProjectDetailSerializer,
    IssueListSerializer,
    IssueDetailSerializer,
    CommentListSerializer,
    CommentDetailSerializer,
)


class MultipleSerializerMixin:
    """_summary_"""
    detail_serializer_class = None

    def get_serializer_class(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class AdminProjectViewSet(MultipleSerializerMixin, ModelViewSet):
    """_summary_"""

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, ]
    filterset_fields = ['id', 'title', 'type', 'author', 'description']
    search_fields = ['title', 'id']

    def get_queryset(self):
        """_summary_"""
        return Projects.objects.all()


class UserViewset(MultipleSerializerMixin, ModelViewSet):
    """_summary_"""
    serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        """_summary_"""
        return User.objects.all()


class ContributorsViewset(MultipleSerializerMixin, ModelViewSet):
    """_summary_

    Args:
        ReadOnlyModelViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """
    serializer_class = ContributorListSerializer
    detail_serializer_class = ContributorDetailSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Contributors.objects.all()


class ProjectsViewset(MultipleSerializerMixin, ModelViewSet):
    """_summary_"""
    
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Projects.objects.all()


class IssuesViewset(MultipleSerializerMixin, ModelViewSet):
    """_summary_

    Args:
        MultipleSerializerMixin (_type_): _description_
        ModelViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Issues.objects.all()


class CommentsViewset(MultipleSerializerMixin, ModelViewSet):
    """_summary_"""
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Comments.objects.all()
