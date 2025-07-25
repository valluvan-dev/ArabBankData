from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Dataset(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='datasets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CustomerEligibility(models.Model):
    customer_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    credit_score = models.IntegerField()
    eligibility_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_id} - {self.name}"
