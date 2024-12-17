from django.db import models
from orders.models import Order
from users.models import User

class Workflow(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    stage = models.CharField(max_length=50, choices=[
        ('printing', 'Printing'),
        ('quality_check', 'Quality Check'),
        ('packaging', 'Packaging'),
        ('ready_for_delivery', 'Ready for Delivery'),
    ])
    assigned_staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)