import smtplib
from email.message import EmailMessage
from getpass import getpass
from collections import defaultdict

if __name__ == "__main__":
    name = input("Name: ")
    n = get_user_input(f"Hi, {name}!\nHow many products do you want to add to the shopping list? ", int)
    shopping_list = defaultdict(int)
    for _ in range(n):
        add_item(shopping_list)
    print_list(shopping_list)

    email = input("Email: ")
    password = getpass("Password: ")
    recipient = input("Recipient's email: ")
    email_to(shopping_list, email, password, recipient)
    
class ShoppingList:
    def __init__(self):
        self.items = defaultdict(int)

    def __str__(self):
        return "\n".join(f"{name} x {quantity}" for name, quantity in self.items.items())

    def add_item(self, name, quantity):
        self.items[name] += quantity

    def email_to(self, from_email, password, *recipients):
        ...

if __name__ == "__main__":
    name = input("Name: ")
    n = get_user_input(f"Hi, {name}!\nHow many products do you want to add to the shopping list? ", int)
    shopping_list = ShoppingList()
    for _ in range(n):
        name = get_user_input("Input the product name: ")
        quantity = get_user_input("Input the product quantity: ", int)
        shopping_list.add_item(name, quantity)
    print(shopping_list)

    email = input("Email: ")
    password = getpass("Password: ")
    recipient = input("Recipient's email: ")
    shopping_list.email_to(email, password, recipient)
