from django.db import models


# Create your models here.
class ActionItem(models.Model):
    text = models.CharField(max_length=300)
    completed = models.BooleanField()

    def __str__(self):
        complete = "Done" if self.is_completed() else "Not Done"
        return f'({complete}) {self.text}'

    def is_completed(self):
        return self.completed

    def swap_status(self):
        self.completed = not self.completed
        self.save(update_fields=["completed"])
