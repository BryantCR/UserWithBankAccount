from BankAccount import BankAccount

class User:

    allUsersAccount = []

    def __init__(self, accountNum, owner):
        self.accountNum = accountNum
        self.owner = owner
        self.balance = BankAccount(interest_rate = 1.003, balance = 0)
        User.allUsersAccount.append( self )

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance.make_withdrawal2(amount)
        else:
            print( "We cannot process your withdrawal." )
            print( f"You currently have {self.balance}." )
            print( f"And you are trying to withdraw {amount}." )
        return self

    def make_deposit( self, amount ):
        self.balance.deposit2(amount)
        return self

    def display_User_Balance(self):
        print( f"User Name: {self.owner}, Balance: ${self.balance.balance}." )
        return self

    # def validateFunds(self, amount):
    #     if self.balance > amount:
    #         return True
    #     else:
    #         return False
    #     return self

    # def transfer_Money(self, owner, amount):
    #     if self.validateFunds(amount):
    #         self.make_withdrawal( amount )
    #         owner.make_deposit( amount )
    #     else:
    #         print( "You don't have enough funds to transfer." )
    #     return self
