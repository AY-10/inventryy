from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = 'SA', _('Super Admin')
        ADMIN = 'AD', _('Admin')

    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.ADMIN,
    )
    email = models.EmailField(unique=True)
    auth0_id = models.CharField(
        max_length=255, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_super_admin(self):
        return self.role == self.Role.SUPER_ADMIN

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN


class UserActivity(models.Model):
    class ActionType(models.TextChoices):
        CREATE = 'CR', _('Create')
        UPDATE = 'UP', _('Update')
        DELETE = 'DL', _('Delete')
        LOGIN = 'LI', _('Login')
        LOGOUT = 'LO', _('Logout')
        PRICE_UPDATE = 'PU', _('Price Update')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='activities')
    action_type = models.CharField(max_length=2, choices=ActionType.choices)
    # e.g., 'Product', 'Store', etc.
    model_name = models.CharField(max_length=50)
    object_id = models.IntegerField()  # ID of the affected object
    # Store additional details about the action
    details = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'User Activities'

    def __str__(self):
        return f"{self.user.username} - {self.get_action_type_display()} - {self.model_name} #{self.object_id}"
