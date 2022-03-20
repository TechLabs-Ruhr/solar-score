from django.db import models

class Client(models.Model):
    id = models.IntegerField("Identifikationsnummer", primary_key=True)
    location = models.CharField("Wohnort", max_length=256)
    p_max = models.DecimalField("Maximale Leistung", decimal_places=3, max_digits=10)

    def __str__(self):
        return self.id