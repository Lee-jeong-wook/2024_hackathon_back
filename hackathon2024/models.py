from django.db import models

class Analyze(models.Model):
    name = models.CharField(max_length=100)
    data = models.TextField()

class Market(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Chat(models.Model):
    user = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)