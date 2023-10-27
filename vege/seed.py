from faker import Faker
import random
from .models import *
fake = Faker()


def seed_db(num=10):
    try:
        for _ in range(num):
            departments_obj = Department.objects.all()
            random_idx = random.randint(0, len(departments_obj)-1)
            department = departments_obj[random_idx]
            student_obj = Student.objects.create(
                dept=department,
                student_id=StudentID.objects.create(
                    student_id=f'STU-0{random.randint(100,999)}'),
                student_name=fake.name(),
                student_email=fake.email(),
                student_age=random.randint(20, 30),
                student_address=fake.address(),
            )
    except Exception as e:
        print(e)
