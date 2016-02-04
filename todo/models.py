from django.db import models
import uuid 
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User)
    token = models.UUIDField(default = uuid.uuid4)

class Todo(models.Model):
    task = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    completed = models.BooleanField(default = False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        return dict(
            id = self.id,
            task=self.task,
            completed=self.completed,
            updated_at = self.updated_at,
            created_at = self.created_at

        )

