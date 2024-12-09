from django.db import models

CATEGORY_CHOICES = [
    ('personal', 'Personal'),
    ('academic', 'Academic'),
    ('deadline', 'Deadline'),
]

class Task(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')  # Add category field

    def __str__(self):
        return self.text
