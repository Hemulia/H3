from django.db import models


class Tool(models.Model):
   name = models.CharField(max_length=200)
   brand = models.CharField(max_length=200)

   def __str__(self):
        return f"{self.name} ({self.brand})"    	
