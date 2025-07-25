from django.core.management.base import BaseCommand
from marketplace.models import CustomerEligibility
from faker import Faker
import random

class Command(BaseCommand):
    help = "Load 200 sample customer eligibility records"

    def handle(self, *args, **kwargs):
        fake = Faker()
        CustomerEligibility.objects.all().delete()  # clean table first
        objs = []
        for _ in range(200):
            objs.append(
                CustomerEligibility(
                    customer_id=fake.uuid4()[:8],
                    name=fake.name(),
                    credit_score=random.randint(300, 850),
                    eligibility_status=random.choice(["Eligible", "Not Eligible"]),
                )
            )
        CustomerEligibility.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS("✅ Loaded 200 sample records!"))
