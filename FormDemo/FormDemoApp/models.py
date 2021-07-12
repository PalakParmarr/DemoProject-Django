from django.db import models
from django.forms import ModelForm
# Create your models here.
class FormModel(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    feedback = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class MyForm(ModelForm):
    class Meta:
        model = FormModel
        exclude = ('date_subscribed','messages_received')