from django.db import models

# Create your models here.
class CustomRequest(models.Model):
    email = models.EmailField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.email} - {self.created_at}"
