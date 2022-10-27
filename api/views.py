from http import server
from rest_framework import viewsets
from .serializer import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer, NotificationSerializer, ReceiptSerializer, TransactionSerializer, WalletSerializer
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Transaction, Wallet
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# Adding an APOI views to controll the behaviour of the deposit
# function and return an appropriate response to the client

class AccountDepositView(views.APIView):
    """
    This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """

    def post(self, request, format=None):
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        try:
            account = Account.objects.get(account_id=account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
        
        message, status = account.deposit(amount)
        return Response(message, status=status)

# Transfer
class AccountTransferView(views.APIView):
    """
    This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """

    def post(self, request, format=None):
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        destination = request.data["destination"]
        try:
            account = Account.objects.get(account_id=account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
        
        message, status = account.transfer(amount, destination)
        return Response(message, status=status)

class AccountWithdrawView(views.APIView):
    """
    This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """

    def post(self, request, format=None):
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        try:
            account = Account.objects.get(account_id=account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
        
        message, status = account.transfer(amount)
        return Response(message, status=status)
