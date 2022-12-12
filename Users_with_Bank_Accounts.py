class User:
    def __init__(self, name="Unassigned", starting_balance=0, interest_rate=0.04):
        self.name = name
        self.account = BankAccount(starting_balance, interest_rate)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self

class BankAccount:

    bank_name = "American Bank"
    all_accounts = []

    def __init__(self, balance=0, interest=0.4):
        self.balance = balance
        self.interest_rate = interest
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            print("Withdrawing $" + str(amount)) 
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Account Balance: $" + str(self.balance))
        print("Interest Rate:", self.interest_rate)
        return self

    def yield_interest(self):
        print("Yielding interest...")
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def all_balances(cls):
        sum = 0

        for account in cls.all_accounts:
            sum += account.balance
        return sum

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        return cls

jesus = User("Jesus Avila")
jesus.display_user_balance().make_deposit(100).display_user_balance()
jesus.make_withdrawal(55).display_user_balance()
jesus.yield_interest().display_user_balance()

jay = User(name="Jay Avila", interest_rate=0.02)
jay.display_user_balance().make_deposit(500)
jay.make_withdrawal(150).display_user_balance()
jay.yield_interest().display_user_balance()

class User:

    def __init__(self, name="Unassigned"):
        self.name = name
        self.accounts = {}

    def open_new_account(self, with_amount=0, interest=0.04, account_type="checking"):
        print("Creating new account..")
        self.accounts[account_type] = BankAccount(with_amount, interest, account_type)
        return self

    def make_withdrawal(self, amount, account_type="checking"):
        self.accounts[account_type].withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        for account_name in self.accounts:
            self.accounts[account_name].display_account_info()
        return self

    def transfer_money(self, other_user, other_user_acc_type, amount, from_account_type):
        if self.accounts[from_account_type].balance < amount:
            print("Insufficient funds")
            return self
        print("Transferring $" + str(amount) + " into " + other_user.name + "'s " + other_user_acc_type + " account.")
        self.accounts[from_account_type].balance -= amount
        other_user.accounts[other_user_acc_type].balance += amount

        self.display_user_balance()
        other_user.display_user_balance()

        return self

    def make_deposit(self, amount, account_type="checking"):
        self.accounts[account_type].deposit(amount)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self

class BankAccount:

    bank_name = "American Bank"
    all_accounts = []

    def __init__(self, balance=0, interest=0.04, account_type="checking"):
        self.balance = balance
        self.interest_rate = interest
        self.account_type = account_type
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            print("Withdrawing $" + str(amount)) 
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Account: ", self.account_type)
        print("Account Balance: $" + str(self.balance))
        print("Interest Rate:", self.interest_rate)
        return self

    def yield_interest(self):
        print("Yielding interest...")
        self.balance += self.balance * self.interest_rate
        return self
    
    @classmethod
    def all_balances(cls):
        sum = 0

        for account in cls.all_accounts:
            sum += account.balance
        return sum

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        return cls

jesus = User("Jesus Avila")
jesus.open_new_account(0, 0.05)
jesus.make_deposit(100).display_user_balance()
jesus.open_new_account(500, 0, "savings")

jay = User("Jay Avila")
jay.open_new_account(300, 0.045).display_user_balance()
jay.transfer_money(sadie, "checking", 100, "checking").make_withdrawal(150).display_user_balance()
print("*"*15)
print("BANK INFO ALL ACCOUNTS")
print("*"*15)
print(BankAccount.print_all().all_balances())

print("*"*15)
print("Making Transfers")
print("*"*15)
jesus.make_deposit(100,"savings").display_user_balance()
jesus.transfer_money(sadie, "checking", 50, "savings").display_user_balance()

jesus.transfer_money(sami, "checking", 100, "savings")

print("*"*15)
print("BANK INFO ALL ACCOUNTS")
print("*"*15)
print(BankAccount.print_all().all_balances())