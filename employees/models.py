from django.db import models

class Employee(models.Model):
    LEVEL_CHOICES = [
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    position = models.CharField(max_length=100, verbose_name="Должность")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Зарплата")
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, verbose_name="Уровень")

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='employees/photos/', blank=True, null=True)
    date_hired = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
