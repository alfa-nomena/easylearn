from owner.models import Owner
from faker import Faker
from tqdm import tqdm
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help = "Create fake data for owners"
    
    def clean_owner(self, *args, **kwargs):
        self.stdout.write("Clean DataBase")
        if Owners:=Owner.objects.all():
            for owner in tqdm(Owners, desc="removing old data from database"):
                owner.delete()
                
    def handle(self, *args, **kwargs):
        self.clean_owner()
        faker = Faker()
        for _ in tqdm(range(10), desc="Creating Owners"):
            user = Owner.objects.create(
                username = faker.user_name(),
                password = "Yalarix0.",
                email = faker.email(),
                first_name = faker.first_name(),
                last_name = faker.last_name()
            )
            user.save()          
        self.stdout.write("Owners created")