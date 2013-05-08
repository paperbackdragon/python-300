import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../2013-UW-python-training/lectures/05-7-2013_advanced_OO/examples/decorators"))
from decorators import logger 

class BankAccount(object):
    def __init__(self, account_number):
        # note that the actual field value is "hidden"
        self._balance = 0.0
        self.account_number = account_number

    def __str__(self):
        return "This account's number is %s" % (self.account_number)

    def __add__(self, other):
        return self.balance + other.balance

    @property
    def balance(self):
        """getter"""
        return self._balance

    @balance.setter
    def balance(self, value):
        # record this transaction
        print "Set the value of account %(account_number)s to %(value)f" % \
            {'account_number': self.account_number, 'value': value}

        # make sure balance is always >= 0
        if value < 0:
            raise ValueError("Value cannot be less than 0.\n")
        
        # set new balance
        self._balance = value
        print "Account %s has balance %.2f\n" % (self.account_number, self.balance)

    def deposit(self, value):
        # record this transaction
        print "Deposit %s into account %s" % (value, self.account_number)

        # add new value to account
        self.balance += value

    def withdraw(self, value):
        # record this transaction
        print "Withdraw %s from account %s" % (value, self.account_number)

        # TODO: make sure withdrawal doesn't allow balance to go below zero

        # add new value to account
        self.balance -= value

class CheckingAccount(BankAccount):
    pass

if __name__ == "__main__":

    account1 = BankAccount("xx")
    account2 = CheckingAccount("zz")

    print account1.__str__()

    account1.balance = 10.0
    try:
        account1.balance = -1
    except ValueError as e:
        print(e)

    account1.deposit(5)
    account1.withdraw(3)

    account2.deposit(20)
    print "Sum of both accounts is: %s" % (account1 + account2)
