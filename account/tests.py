from django.test import TestCase
from .models import  Account
from django.core.exceptions import ObjectDoesNotExist

# Create your tests here.
class AccountTestCase(TestCase):

    def setUp(self):
        Account.objects.create(name="lion", email="vanphudhsp2015@gmail.com")
       

    def test_account_can_speak(self):
        """Animals that can speak are correctly identified"""
        try:
            admin = Account.objects.get(email="vanphudhsp2015@gmail.com")
            print(admin)
        except ObjectDoesNotExist:
            print("Error")
    
    def test_account_can_all(self):
        try:
            listaccount = Account.objects.all()
            for i in listaccount:
                print(i)
        except ObjectDoesNotExist:
            print("Error")

    def test_account_can_admin(self):
        try:
            admin = Account.objects.filter(email="vanphudhsp2015@gmail.com",author="account")
            if(admin.count() > 1 ):
                print('Is Admin')
            else:
                print('Isnt Admin')
        except ObjectDoesNotExist:
            print("Error")

    def for_get(selt):
        