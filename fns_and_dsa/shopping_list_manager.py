shopping_list = []

while True:
    menu = int(input("Enter 1 to add item,2 to remove item,3 to print list,4 to exit: "))
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
         
