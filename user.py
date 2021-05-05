class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance:{self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
yuri = User("Yuri Bytheway", "yuri@python.com")


guido.make_deposit(100).make_deposit(800).make_deposit(100).make_withdrawal(200).display_user_balance()
monty.make_deposit(50).make_deposit(580).make_withdrawal(25).make_withdrawal(15).display_user_balance()
yuri.make_deposit(580).make_withdrawal(25).make_withdrawal(15).make_withdrawal(15).display_user_balance()


guido.transfer_money(yuri, 1200)
guido.display_user_balance()
yuri.display_user_balance()


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
mark = User("Mark Albiston", "mark@me.com")

