def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    return "Choose one option"
shopping_list = []

while True:
    menu = int(input(display_menu()))
    if menu == 1:
        newitem = input("Enter the new item: ")
        shopping_list.append(newitem)
        
    elif menu == 2:
        remitem = input("Enter item to remove: ")
        if remitem in shopping_list:
            shopping_list.remove(remitem)
        else:
            print("Item not found in the list.")
        
        
    elif menu == 3:
        for i in shopping_list:
            print(i)
            
    elif menu == 4:
        print("Bye,user")
        break
    
    else:
        print("Enter a valid task")
         
         
