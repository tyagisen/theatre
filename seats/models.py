from django.db import models
# from django.contrib.auth


class Seats(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return f"row {self.row} column {self.column}"
