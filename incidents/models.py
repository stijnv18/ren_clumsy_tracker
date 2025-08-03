from django.db import models

# Create your models here.

class Incident(models.Model):
    friend_name = models.CharField(max_length=100, default="Ren")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    CLUMSY_LEVELS = [
        (1, "Minor"),
        (2, "Noticeable"),
        (3, "Major"),
        (4, "Legendary")
    ]
    clumsy_level = models.IntegerField(choices=CLUMSY_LEVELS)

    def __str__(self):
        return f"{self.friend_name} - {self.date} - {self.get_clumsy_level_display()}"

# Create your models here.
