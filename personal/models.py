from django.db import models

# Create your models here.

# Choices for priority levels for questions
PRIORITY = [("L", "Low"), ("M", "Medium"), ("H", "High")]

# Question model representing a question
class Question(models.Model):
    title = models.CharField(max_length = 60)
    question = models.TextField(max_length = 400)
    priority = models.CharField(max_length = 1, choices = PRIORITY)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "List of Questions"
        verbose_name_plural = "User's Questions"