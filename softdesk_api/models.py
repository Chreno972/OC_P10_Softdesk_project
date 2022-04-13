"""
Models module for the softdesk_api application.
"""
from django.db import models


class User(models.Model):
    """Model for a user"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name)


class Contributors(models.Model):
    """Model for a contributor"""

    PERMISSIONS = (
        ("admin", "Admin"),
        ("contributor", "Contributor"),
    )

    project = models.ForeignKey(
        "Projects",
        on_delete=models.CASCADE,
        related_name="contributors",
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="contributors",
    )

    permission = models.CharField(max_length=255)
    role = models.CharField(
        max_length=50,
        choices=PERMISSIONS,
        default="contributor"
        )
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.permission)


class Projects(models.Model):
    """Model for a project"""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=255)
    author = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="projects"
    )
    active = models.BooleanField(default=False)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return str(self.title)


class Issues(models.Model):
    """Model for an issue"""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    author = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="issues",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return str(self.title)


class Comments(models.Model):
    """Model for a comment"""

    description = models.TextField(blank=True)
    author_user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="author_id",
    )
    issue_id = models.ForeignKey(
        "Issues",
        on_delete=models.CASCADE,
        related_name="issues_id",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        return str(self.description)
