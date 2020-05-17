from django.db import models

class ContactDetails(models.Model):
     
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return str(self.id)

