class BankAccount:

    initInfo = []

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.initInfo.append(self)

    def deposit( self, amount ):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print( "Insufficient funds: Charging a $5 fee" )
            self.balance -= 5
        return self

    def display_Account_Info(self):
        print( f"Balance: ${self.balance}" )
        return self

    def yield_interes(self, interest_rate):
        if self.balance > 0:
            self.balance = self.balance * self.interest_rate
        return self

    def allInfo(self):
        print(f"Balance: ${self.balance}, Interes rate: {self.interest_rate} " )

    @classmethod
    def printAllAccountsInfo(cls):
        print(f"This is the information for all the accounts")
        for account in cls.initInfo:
            account.user.printUserInfo()
            account.allInfo()
