from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StudentManagement(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Recipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="images/")
    view_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ["department"]


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id


class Student(models.Model):
    dept = models.ForeignKey(
        Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(
        StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)

    objects = StudentManagement()
    admin_objects = models.Manager()

    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

    def __str__(self) -> str:
        return self.student_name
