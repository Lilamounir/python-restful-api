shoppingList = []
        
def help_instruc():
    print("-------------------------------------------------------")
    print("type DONE to finish the list                           |")
    print("type SHOW to show the list                             |")
    print("type HELP for a help message about these commands      |")
    print("-------------------------------------------------------")

    
def print_shopping_list():
    print("---------------")
    print("Shopping List:")
    print("---------------")
    for item in shoppingList:
        print("> " + item)
        
def add_item_to_list(item):
    shoppingList.append(item)
    print("-------------------------------------------------------")
    print("Added {} to shopping list! List now has {} items".format(item, len(shoppingList)))
    
def main():   
    help_instruc()
    while True:
        item = str(input("Enter an item to add to the list... "))
        if item == 'DONE':
            print_shopping_list()
            break
        elif item == 'SHOW':
            print_shopping_list()
        elif item == 'HELP':
            help_instruc()
        else:
            add_item_to_list(item)
            
main()
