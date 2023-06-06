from django.db import models
# from django.contrib.auth

class Theatre(models.Model):
    name = models.CharField(max_length=255)


class CustomerSeat(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"row {self.row} column {self.column}"
