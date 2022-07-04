from django.db import models

class Subject(models.Model):

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"

    def __str__(self):
        return self.name

    name = models.CharField(verbose_name="Назва",
                            max_length=100,
                            blank=True,
                            null=True)



class StudentGroup(models.Model):
    name = models.CharField(verbose_name="Имя",
                            max_length=100)
    subjects = models.ManyToManyField(Subject,
                                    verbose_name="Предмети",
                                    #on_delete=models.SET_NULL,
                                    related_name="subjects",
                                    blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа студентов"
        verbose_name_plural = "Группы студентов"


class Student(models.Model):

    SURNAME_CHOICES = (
        ('Petrenko', 'Петренко'),
        ('Ivanenko', 'Іваненко'),
    )

    name = models.CharField(verbose_name="Имя",
                            max_length=100,
                            blank=True,
                            null=True)
    surname = models.CharField(verbose_name="Фамилия",
                            max_length=100,
                            blank=True,
                            null=True,
                            choices=SURNAME_CHOICES)
    birthday = models.DateField(verbose_name="День рождения",
                                null=True,
                                blank=True)
    group = models.ForeignKey(StudentGroup, verbose_name="Группа",
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="students",
                                    blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # self.name += '111'
        super().save(*args, **kwargs)
        # self.name += '55555555'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
