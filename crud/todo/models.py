from django.db import models

# Create your models here.

# declare a new model
class TodoApp(models.Model):

    # fields of the model
    # charfield means character field
    title = models.CharField(max_length=200)
    # textfield have not limit
    description = models.TextField()

    # used to name our object. dungant method __str__
    # want the title to show in the database
    def __str__(self):
        return self.title
