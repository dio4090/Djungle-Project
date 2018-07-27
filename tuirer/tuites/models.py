from django.db import models
from tuites.managers import TuitesManager

# Create your models here.
class Tuite(models.Model):
    content = models.CharField(max_length=280)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='Diogo')
    created_date = models.DateTimeField(auto_now_add=True)
    
    objects = TuitesManager
    
    def str(self):
        return f'{self.author.username}: {self.content}'

    class Meta:
        ordering = ('-content', )
