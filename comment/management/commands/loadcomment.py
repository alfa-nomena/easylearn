from faker import Faker
from tqdm import tqdm
from django.core.management.base import BaseCommand
from comment.models import Comment
import random
from course.models import Course
from owner.models import Owner


class Command(BaseCommand):
    help = "Create fake data for comments"
    
    def clean_comment(self, *args, **kwargs):
        self.stdout.write("Clean DataBase")
        if comments:=Comment.objects.all():
            for comment in tqdm(comments, desc="removing old data from database"):
                comment.delete()
                
    def handle(self, *args, **kwargs):
        self.clean_comment()
        faker = Faker()
        courses = Course.objects.all()
        for course in tqdm(courses, desc="Creating comments"):
            for _ in range(random.randrange(0,20)):
                comment = Comment(
                    course=course,
                    owner = Owner.objects.all().order_by("?").first(),
                    content = faker.text(random.randrange(10,500))
                )
                comment.save()
        self.stdout.write("comments created")