from django.shortcuts import render, redirect
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RecieptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

# Create your views here.


def register_customer(request):
    if request.method == 'POST':
        # initializing the form by creating an instance
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request, 'wallet/register_customer.html', {'form': form})


def register_wallet(request):
    if request.method == 'POST':
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()  # initializing the form by
    return render(request, 'wallet/register_wallet.html', {'form': form})


def create_account(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(
            request.POST)  # initializing the form by
        if form.is_valid():
            form.save()
    else:
        form = AccountRegistrationForm()
    return render(request, 'wallet/create_account.html', {'form': form})


def create_reward(request):
    if request.method == 'POST':
        form = RewardRegistrationForm(request.POST)  # initializing the form by
        if form.is_valid():
            form.save()
    else:
        form = RewardRegistrationForm()  # initializing the form by
    return render(request, 'wallet/create_reward.html', {'form': form})


def create_transaction(request):
    if request.method == 'POST':
        form = TransactionRegistrationForm(
            request.POST)  # initializing the form by
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request, 'wallet/create_transaction.html', {'form': form})


def create_card(request):
    if request.method == 'POST':
        form = CardRegistrationForm(request.POST)  # initializing the form by
        if form.is_valid():
            form.save()
    else:
        form = CardRegistrationForm()  # initializing the form by
    return render(request, 'wallet/create_card.html', {'form': form})


def create_notification(request):
    if request.method == 'POST':
        form = NotificationRegistrationForm(
            request.POST)  # initializing the form by
        if form.is_valid():
            form.save()
    else:
        form = NotificationRegistrationForm()  # initializing the form
    return render(request, 'wallet/create_notification.html', {'form': form})


def create_receipt(request):
    if request.method == 'POST':
        form = RecieptRegistrationForm(request.POST)  # initializing the form
        if form.is_valid():
            form.save()
    else:
        form = RecieptRegistrationForm()  # initializing the form
    return render(request, 'wallet/create_receipt.html', {'form': form})


def request_loan(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()  # initializing the forms
    return render(request, 'wallet/request_loan.html', {'form': form})


def create_third_party(request):
    if request.method == 'POST':
        form = ThirdPartyRegistrationForm(request.POST)  # initializing the
        if form.is_valid():
            form.save()
    else:
        form = ThirdPartyRegistrationForm()  # initializing the forms
    return render(request, 'wallet/create_third_party.html', {'form': form})


def register_currency(request):
    if request.method == 'POST':
        form = CurrencyRegistrationForm(request.POST)  # initializing the forms
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()  # initializing the forms
    return render(request, 'wallet/register_currency.html', {'form': form})

# Displaying the list of customers
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'wallet/customer.html', {'customers': customers})


def wallet_list(request):
    wallets = Wallet.objects.all()
    return render(request, 'wallet/wallet_list.html', {'wallets': wallets})


def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'wallet/account_list.html', {'accounts': accounts})


def reward_list(request):
    rewards = Reward.objects.all()
    return render(request, 'wallet/reward_list.html', {'rewards': rewards})


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'wallet/transactions.html', {'transactions': transactions})


def card_list(request):
    cards = Card.objects.all()
    return render(request, 'wallet/cards.html', {'cards': cards})


def notifcation_list(request):
    notifications = Notification.objects.all()
    return render(request, 'wallet/notifications.html', {'notifications': notifications})


def receipt_list(request):
    receipts = Receipt.objects.all()
    return render(request, 'wallet/receipts.html', {'receipts': receipts})


def loan_list(request):
    loans = Loan.objects.all()
    return render(request, 'wallet/loans.html', {'loans': loans})


def third_party_list(request):
    third_partys = ThirdParty.objects.all()
    return render(request, 'wallet/third_party_list.html', {'third_partys': third_partys})


def currency_list(request):
    curencies = Currency.objects.all()
    return render(request, 'wallet/currency_list.html', {'curencies': curencies})


# Displaying a single view
def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'wallet/customer-profile.html', {'customer': customer})

def wallet_display(request, id):
    wallet = Wallet.objects.get(id=id)
    return render(request, 'wallet/wallet-display.html', {'wallet': wallet})

def account_display(request, id):
    account = Account.objects.get(id=id)
    return render(request, 'wallet/account-display.html', {'account': account})

def card_display(request, id):
    card = Card.objects.get(id=id)
    return render(request, 'wallet/card-display.html', {'card': card})

def transaction_display(request, id):
    transaction = Transaction.objects.get(id=id)
    return render(request, 'wallet/transaction-display.html', {'transaction': transaction})

def receipt_display(request, id):
    receipt = Receipt.objects.get(id=id)
    return render(request, 'wallet/receipt-display.html',   {'receipt': receipt})    


# Editing the customer profile
def edit_customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile', id=customer.id)

    else:
        form = CustomerRegistrationForm(instance=customer)
        return render(request, 'wallet/edit_customer.html', {'form': form})

def edit_wallet(request, id):
    wallet = Wallet.objects.get(id=id)
    if request.method == 'POST':
        form = WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect('profile', id=wallet.id)

    else:
        form = WalletRegistrationForm(instance=wallet)
        return render(request, 'wallet/edit_wallet.html', {'form': form})

def edit_account(request, id):
    account = Account.objects.get(id=id)
    if request.method == 'POST':
        form = AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('profile', id=account.id)

    else:
        form = AccountRegistrationForm(instance=account)
        return render(request, 'wallet/edit_account.html', {'form': form})

def edit_receipt(request, id):
    receipt = Receipt.objects.get(id=id)
    if request.method == 'POST':
        form = ReceiptRegistrationForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('profile', id=receipt.id)

    else:
        form = ReceiptRegistrationForm(instance=receipt)
        return render(request, 'wallet/edit_receipt.html', {'form': form})

def edit_card(request, id):
    card = Card.objects.get(id=id)
    if request.method == 'POST':
        form = CardRegistrationForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('profile', id=card.id)

    else:
        form = CardRegistrationForm(instance=card)
        return render(request, 'wallet/edit_card.html', {'form': form})

def edit_transaction(request, id):
    transact = Transaction.objects.get(id=id)
    if request.method == 'POST':
        form = TransactionRegistrationForm(request.POST, instance=transact)
        if form.is_valid():
            form.save()
            return redirect('profile', id=transact.id)

    else:
        form = CardRegistrationForm(instance=transact)
        return render(request, 'wallet/edit_transact.html', {'form': form})
