from django.db import models


# Create your models here.
class Task(models.Model):

    LIST_TYPES = [
        ('D', 'daily'),
        ('W', 'weekly'),
        ('M', 'monthly')
    ]

    text = models.CharField(max_length=300)
    completed = models.BooleanField()
    list_type = models.CharField(max_length=1, choices=LIST_TYPES, default="W")
    user_id = models.IntegerField(default=0)

    def __str__(self):
        complete = "Done" if self.is_completed() else "Not Done"
        return f'({complete}) {self.text} - User {self.user_id}'

    def is_completed(self):
        return self.completed

    def swap_status(self):
        self.completed = not self.completed
        self.save(update_fields=["completed"])
