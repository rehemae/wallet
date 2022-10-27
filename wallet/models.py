import datetime
from email.policy import default
from random import choices
from django.db import models


# Create your models here.

marital_status = (('Married'), ('Single'), ('Divorced'))
transact = (('Deposit'), ('Withdraw'))
loanStatus = (('Pending'), ('Accepted'), ('Rejected'))


class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=15)
    id_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    # profile = models.ImageField()
    # signature = models.ImageField()
    employment_status = models.BooleanField(default=False)
    marital_status = models.CharField(
        max_length=20, null=True)

    # def __str__(self):
    #     return self.first_name


class Wallet(models.Model):
    customer = models.OneToOneField(
        'Customer', on_delete=models.DO_NOTHING, related_name='customer')
    date = models.DateTimeField(default=datetime.datetime.now)
    pin = models.IntegerField()
    is_active = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=20, decimal_places=2)

    # def __str__(self):
    #     return self.customer


class Account(models.Model):
    acc_type = models.CharField(max_length=255, blank=True)
    acc_name = models.CharField(max_length=255, blank=True)
    savings = models.IntegerField(default=0)
    acc_balance = models.IntegerField(default=0)
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    destination = models.CharField(max_length=255, blank=True)

    # Adding deposit functionality to account model
    def deposit(self, amount):
        if amount <= 0:
            message = "Invalid amount"
            status = 403
        else:
            self.account_balance += amount
            self.save()
            message = f"You have deposited {amount}, your new balance is {self.acc_balance}"
            status = 200
        return message, status

        # Let’s add another method in the account model to
        # transfer funds to another account to another.
    def transfer(self, destination, amount):
       if amount <= 0:
           message = "Invalid amount"
           status = 403

       elif amount < self.account_balance:
           message = "Insufficient balance"
           status = 403

       else:
           self.account_balance -= amount
           self.save()
           destination.deposit(amount)

           message = f"You have transfered {amount}, your new balance is {self.account_balance}"
           status = 200
       return message, status

# Withdraw functionality
    def withdraw(self, amount):
        if amount <= 0:
            message = "Invalid amount"
            status = 403
        else:
            self.account_balance -= amount
            self.save()
            message = f"You have withdrawn {amount}, your new balance is {self.acc_balance}"
            status = 200
        return message, status

    #  Request loan functionality
    def request_loan(self, amount):
        if amount<= 0:
            message = "Invalid amount"
            status = 403
        else:
            self.acc_balance += amount
            self.save()
            message = f"Your "

    


class Reward(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,default=False,blank=True)
    points = models.IntegerField(default=False)
    date_time = models.DateTimeField(null=True)
    transaction = models.ForeignKey('Transaction',on_delete=models.CASCADE,default=False, blank=True)

class Transaction (models.Model):
    date_time = models.DateTimeField(null = True)
    amount = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=15,blank=True, default=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, default=False)
    transaction_code = models.CharField(max_length=15,blank=True, default=False)
    charge = models.IntegerField(default=0)
    status = models.CharField(max_length=15,blank=True, default=False)
    origin_account = models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Transaction_Receipt",blank=True, default=False)
    destination_account = models.ForeignKey("Account", on_delete=models.CASCADE,default=False, blank=True)

    # def __str__(self):
    #     return self.transaction_type

class Card(models.Model):
    card_number = models.CharField(max_length=25, blank=True)
    card_name = models.CharField(max_length=25, blank=True)
    card_account = models.ForeignKey('Account', on_delete=models.CASCADE)
    pin_number = models.CharField(max_length=5, blank=True)
    security_code = models.CharField(max_length=5, blank=True)

    # def __str__(self):
    #     return self.card_name


class Notification(models.Model):
    message = models.TextField()
    date_time = models.DateTimeField(null=True, blank=True)
    recipient = models.ForeignKey(
        'Customer', blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='customer_notification')

    # def __str__(self):
    #     return self.date_time


class Receipt(models.Model):
    # receipt_file = models.FileField()
    receipt_date = models.DateTimeField(default=datetime.datetime.now)
    total_amount = models.PositiveIntegerField()
    transaction = models.ForeignKey(
        'Transaction',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='receipt_transaction'
    )



class Loan(models.Model):
    amount = models.PositiveIntegerField()
    borrow_date_and_time = models.DateTimeField(default="")
    wallet = models.ForeignKey(
        'Wallet',
        on_delete=models.CASCADE,
        related_name='wallet_loan'
    )
    interest_rate = models.PositiveIntegerField()
    guarantee = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        related_name='customer_loan'
    )
    payment_due_date = models.DateTimeField(
        null=True,
        blank=True)
    loan_balance = models.PositiveIntegerField()
    loan_term = models.TextField()
    loan_status = models.CharField(
        max_length=15,
        default="Unpaid",
        null=True
    )
    duration = models.PositiveIntegerField()

    # def __str__(self):
    #     return self.wallet


class ThirdParty(models.Model):
    fullname = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    transaction_cost = models.IntegerField()
    currency = models.OneToOneField(
        'Currency', max_length=20, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, blank=True)
    account = models.ForeignKey(
        'Account', blank=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.fullname

class Currency(models.Model):
    country = models.CharField(max_length=25)
    symbol = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=25, blank=True)

    # def __str__(self):
    #     return self.name