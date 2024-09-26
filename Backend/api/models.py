from django.db import models

class Notes(models.Model):
    CATEGORY_CHOICES = [
        ('Science', 'Science'),
        ('Mathematics', 'Mathematics'),
        ('Literature', 'Literature'),
        ('Others', 'Others'),

    ]

    title = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=400)
    price = models.FloatField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='notes/', null=True, blank=True)

    def __str__(self):
        return self.title