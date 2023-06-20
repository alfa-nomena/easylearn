from course.models import Course
from faker import Faker
from tqdm import tqdm
from django.core.management.base import BaseCommand

import random


class Command(BaseCommand):
    help = "Create fake data for courses"
    
    def clean_course(self, *args, **kwargs):
        self.stdout.write("Clean DataBase")
        if courses:=Course.objects.all():
            for course in tqdm(courses, desc="removing old data from database"):
                course.delete()
                
    def handle(self, *args, **kwargs):
        self.clean_course()
        faker = Faker()
        for _ in tqdm(range(100), desc="Creating courses"):
            course = Course(
                title = faker.text(100),
                content = faker.text(2000),
                date_posted = faker.date()
            )
            course.save()
        self.stdout.write("Courses created")