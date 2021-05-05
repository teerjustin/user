class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0
    def make_deposit(self, amount):
    	self.account_balance += amount
    def make_withdrawal(self, amount):
    	self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance:{self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
yuri = User("Yuri Bytheway", "yuri@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python
print(yuri.name)    #output: Yuri Bytheway

guido.make_deposit(100)
guido.make_deposit(800)
guido.make_deposit(100)
guido.make_withdrawal(200)
monty.make_deposit(50)
monty.make_deposit(580)
monty.make_withdrawal(25)
monty.make_withdrawal(15)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50
guido.make_withdrawal(55)
print(guido.display_user_balance())
print(monty.display_user_balance())

yuri.make_deposit(580)
yuri.make_withdrawal(25)
yuri.make_withdrawal(15)
yuri.make_withdrawal(15)
print(yuri.display_user_balance())

guido.transfer_money(yuri, 800)
print(guido.display_user_balance())
print(yuri.display_user_balance())
