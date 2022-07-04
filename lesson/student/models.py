from django.db import models

class Student(models.Model):
    name = models.CharField(verbose_name="Ім'я'",
                            max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"
        
