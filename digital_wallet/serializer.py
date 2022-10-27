from restframework import Seializer
from wallet.models import Customer

class CustomerResiallizer(models.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email')

