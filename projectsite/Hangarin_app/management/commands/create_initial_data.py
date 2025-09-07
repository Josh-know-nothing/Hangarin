from django.core.management.base import BaseCommand
from faker import Faker
from Hangarin_app.models import Task, Note, SubTask, Priority, Category
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Create initial data for Hangarin'


    def handle(self, *args, **kwargs):
        fake = Faker()
        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        for _ in range(20):  
            task = Task.objects.create(
                task_title=fake.sentence(nb_words=5),
                descript=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                priority=random.choice(priorities),
                category=random.choice(categories),
                deadline=timezone.make_aware(fake.date_time_this_month()),
            )

            
            for _ in range(random.randint(1, 3)):
                Note.objects.create(
                    task=task,
                    contents=fake.paragraph(nb_sentences=2)
                )

        
            for _ in range(random.randint(1, 4)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"])
                )

        self.stdout.write(self.style.SUCCESS(" data generated successfully!"))