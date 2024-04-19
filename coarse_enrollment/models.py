from django.db import models
from account.models import CustomUser
from coarse.models import Coarse
from coarse_content.models import  CoarseContent


class CoarseEnrollment(models.Model):

    ENROLLMENT_STATUS = (
        ('PENDING', 'Pending'),
        ('REVOKED', 'Revoked'),
        ('COMPLETED', 'Completed')
    )

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    coarse = models.ForeignKey(Coarse,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=10,choices=ENROLLMENT_STATUS,default='PENDING')
    progress = models.DecimalField(max_digits=3, decimal_places=3,null=True)
    last_content_accessed = models.ForeignKey(CoarseContent,on_delete=models.CASCADE,null=True),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status