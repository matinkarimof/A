from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} --- {self.created_at} --- {self.is_done}"