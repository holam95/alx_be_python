Task = input("Enter your task:")
Priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes or no):")

match priority:
    case "high":
        if priority == "high" and time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("pay attention to this first")
            
            
            
    case "medium":
        if priority == "medium" and time_bound == "yes":
            print("medium priority but time bound")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
            
    case "low":
         if priority == "low" and time_bound == "yes":
            print("low priority but time bound")
         else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
            
        
