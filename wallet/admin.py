from django.contrib import admin
from .models import Customer, Loan,Notification, Receipt, Reward
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import ThirdParty
from .models import Currency
from .models import Card
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name")

admin.site.register(Customer, CustomerAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ("customer", "balance", "date")
    search_fields = ("customer","balance")
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("acc_name", "acc_type", "savings")
    search_fields = ("acc_name","acc_type")
admin.site.register(Account, AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date_time','transaction_type','amount')
    search_fields = ("date_time","transaction_type")
admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name','card_account',  'card_number')
    search_fields= ('card_number','card_name')
admin.site.register(Card, CardAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('date_time','recipient')
    search_fields= ('date_time','recipient')
admin.site.register(Notification, NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_date','transaction', 'total_amount')
    search_fields= ('receipt_date','receipt_file')
admin.site.register(Receipt, ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('borrow_date_and_time', 'wallet','amount', 'guarantee', 'payment_due_date', 'loan_balance', 'duration')
    search_fields= ('borrow_date_and_time','wallet')
admin.site.register(Loan, LoanAdmin)


class RewardAdmin(admin.ModelAdmin):
    list_display = ('points', 'date_time')
    search_fields= ('wallet','date_time')
admin.site.register(Reward, RewardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    lisr_display = ('fullname', 'email', 'phoneNumber')
    search_fields = ("fullname", "email", "phoneNumber")
admin.site.register(ThirdParty, ThirdPartyAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country', 'name', 'symbol')
    search_fields = ("symbol", "country", "name")
admin.site.register(Currency, CurrencyAdmin)