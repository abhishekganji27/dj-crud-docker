from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=20)
    rp_id = models.IntegerField()

    def __str__(self) -> str:
        return str(self.name)