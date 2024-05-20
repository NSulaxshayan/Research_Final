from django.db import models


class NetworkCapture(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    protocol = models.CharField(max_length=20)
    source_ip = models.CharField(max_length=15)
    destination_ip = models.CharField(max_length=15)
    length = models.IntegerField()

    def __str__(self):
        return f"{self.protocol} {self.source_ip} -> {self.destination_ip}"
