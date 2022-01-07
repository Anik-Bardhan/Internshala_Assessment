from django.db import models
import uuid, datetime
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    email = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name