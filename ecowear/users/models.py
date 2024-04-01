from django.db import models

class User(models.Model):
    USER_GROUP_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=33, unique=True)
    firstName = models.CharField(max_length=33, blank=True)
    lastName = models.CharField(max_length=33, blank=True)
    email = models.EmailField(max_length=33, blank=True)
    password = models.CharField(max_length=33)
    address = models.CharField(max_length=99, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    profilePicture = models.URLField(max_length=255, blank=True)
    userGroup = models.CharField(max_length=5, choices=USER_GROUP_CHOICES)
    userRating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    registerDate = models.DateField(null=True, blank=True)
    lastLoginDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "User"
