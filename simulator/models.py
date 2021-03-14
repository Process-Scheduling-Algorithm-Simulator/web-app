from django.db import models

# Create your models here.

class CpuAlgo(models.Model):
    algo_id = models.IntegerField() 
    algo_name = models.CharField(max_length=50)
    algo_description = models.TextField()

    def __str__(self):
        return self.algo_name
