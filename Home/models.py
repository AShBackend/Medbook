from django.db import models

class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Subject = models.CharField(max_length=50)
    Text = models.TextField()
    Creates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Subject
