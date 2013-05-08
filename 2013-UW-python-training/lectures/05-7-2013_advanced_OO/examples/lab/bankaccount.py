class BankAccount(object):
    def __init__(self, account_number):
        # note that the actual field value is "hidden"
        self._balance = 0.0
        self.account_number = account_number

    @property
    def balance(self):
        """getter"""
        return self._balance

    @balance.setter
    def balance(self, value):
        # record this transaction
        print "set the value of account %(account_number)s to %(value)f" % \
            {'account_number': self.account_number, 'value': value}
        self._balance = value

if __name__ == "__main__":
    account1 = BankAccount("xx")
    account2 = BankAccount("zz")

    print "Account %s has balance %.2f" % (account1.account_number, account1.balance)
    account1.balance = 10.0

