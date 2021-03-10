class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def make_deposit(self, amount):
        self.amount += amount
        return self
        
    def make_withdrawal(self,amount):
        self.amount -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.amount}")
        return self
        
    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        return self

user1 = User("Nathan Bludworth", 0.00)
user2 = User("Edward Smith", 0.00)
user3 = User("Peon Green", 0.00)

# user1.make_deposit(200)
# user1.make_deposit(100)
# user1.make_deposit(300)
# user1.make_withdrawal(400)
# user1.display_user_balance()
user1.make_deposit(200).make_deposit(100).make_deposit(300).make_withdrawal(400).display_user_balance()
# user2.make_deposit(500)
# user2.make_deposit(500)
# user2.make_withdrawal(200)
# user2.make_withdrawal(200)
# user2.display_user_balance()
user2.make_deposit(500).make_deposit(500).make_withdrawal(200).make_withdrawal(200).display_user_balance()
# user3.make_deposit(1000)
# user3.make_withdrawal(200)
# user3.make_withdrawal(200)
# user3.make_withdrawal(200)
# user3.display_user_balance()
user3.make_deposit(1000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).display_user_balance()
# user1.transfer_money(user3, 100)
# user1.display_user_balance()
# user3.display_user_balance()
user1.transfer_money(user3, 100).display_user_balance()
user3.display_user_balance()