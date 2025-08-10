from django.db import models
from django.contrib.auth.models import User

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100, unique=True)
    subscription_plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    settings = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class TenantUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    permissions = models.JSONField(default=list)
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        null=True,  # Temporary
        blank=True,  # Temporary
        related_name='tenant_users'
    )

    class Meta:
        unique_together = ('user', 'tenant')