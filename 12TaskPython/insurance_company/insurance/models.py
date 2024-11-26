from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Policy(models.Model):
    POLICY_TYPES = [
        ('Auto', 'Автострахование'),
        ('Health', 'Медицинская страховка'),
        ('Property', 'Страхование недвижимости'),
    ]

    policy_number = models.CharField(max_length=20, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.policy_number

class Claim(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    claim_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Claim for {self.policy.policy_number} on {self.claim_date}"