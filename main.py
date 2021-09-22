from BankAccount import BankAccount
from User import User


juanAccount = User(12345, "Juan Gomez")
#mariaUser = User(55555. "Maria Lopez", 1.005)
#rodolfoUser = User(78787, "Rodolfo Mora", 1.004)

#print(juanAccount)
#juanAccount.display_User_Balance()

#juanAccount.make_deposit(1000).display_User_Balance()
juanAccount.make_deposit(500).make_deposit(300).display_User_Balance().make_deposit(100).display_User_Balance()
