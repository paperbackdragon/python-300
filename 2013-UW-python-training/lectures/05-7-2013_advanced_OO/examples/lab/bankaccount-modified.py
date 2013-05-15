import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),"../decorators"))
from decorators import logger

class BankAccount(object):
    def __init__(self, account_number):
        # note that the actual field value is "hidden"
        self._balance = 0.0
        self.account_number = account_number

    def __str__(self):
        return "BankAccount number %s" % self.account_number

    def __add__(self, other):

        return self.balance + other.balance

    def __div__(self,other):
        pass


    @property
    def balance(self):
        """getter"""
        return self._balance

    @logger
    def deposit(self, value):
        if value < 0:
            raise ValueError
        self.balance += value
    
    def withdraw(self,value):
        newvalue = self.balance - value
        if newvalue < 0:
            raise ValueError("insufficient funds")
        else:
            self.balance = newvalue

    @balance.setter
    def balance(self, value):
        # record this transaction
       
        # manager says balance has to be above 0
        if value < 0:
            raise ValueError("invalid balance")
        self._balance = value
        print "set the value of account %(account_number)s to %(value)f" % \
            {'account_number': self.account_number, 'value': value}

class CheckingAccount(BankAccount):
    pass

if __name__ == "__main__":
    account1 = CheckingAccount("xx")
    account2 = BankAccount("zz")

    print "Account %s has balance %.2f" % (account1.account_number, account1.balance)
    account1.balance = 10.0
    try:
        # account1.balance = -10.0
        account1.deposit(20)
        account1.deposit(20)
        account2.deposit(33)
        # account1.withdraw(700)
        print "adding two accounts"
        print account1.__class__
        print account2.__class__
        print account1 + account2

        print account1.balance

    except ValueError as e:
        print "invalid value"