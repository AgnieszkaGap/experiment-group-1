class BankAccount:
    AccountNumber=0
    Balance=0

    def createBankAccount(accountNumber, balance):
        account = BankAccount()
        account.AccountNumber = accountNumber
        account.Balance=balance
        print("Accout sucessfully created")

    def deposit(self, deposit):
        if deposit>0:
            self.Balance += deposit
            print("Deposit sucessfully added")
        else:
            print("Please, provide correct deposit amount")

    def withdrawal(self, withdrawal):
        if withdrawal >0 & withdrawal <= self.Balance:
            self.Balance -= withdrawal
            print("Sucessfully withdrawaled")
        else:
            print("Please, provide correct withdrawal amount")





