import BankAccount

class AccountManager:
    accounts=[]

    def addAccount(account):
        accounts.append(account)

    def summary():
        print(accounts)

def transfer(account1, account2, amount):
    if amount > 0 and account1.Balance >= amount:
        account1.Balance -= amount
        account2.Balance += amount


