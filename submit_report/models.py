from django.db import models

# Create your models here.
class Chapel_member(models.Model):
    name= models.CharField(max_length=200, help_text="Enter your name")
    report= models.TextField(help_text='Enter your report')

    def __str__(self):
        return f"{self.name}'s report"

