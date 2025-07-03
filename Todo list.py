def show_menu():
    print('''
What action would you like to perform?
    1. Add new tasks to the list
    2. Clear a completed task from the list
    3. Delete the entire list
      ''')

name = input('Enter you name: ')
listName = input('What do you want to save this list as? ')
show_menu()


todo_list = {}

choice = input('Enter the number that corresponds to your choice: ')
again = ''

try:
    while (int(choice) <= 3) or (again.lower() == 'y'):
        match int(choice):
            case 1:
                date = input('\nEnter the task deadline (DD-MM-YY HH:MM): ')
                task = input('Enter the task details: ')
                todo_list.update({date : task})
                

            case 2:
                date = input('\nEnter the date and time of the completed task: ')
                if date in todo_list:
                    del todo_list[date]
                    print("Task removed.")
                else:
                    print("Task not found.")
                

            case 3:
                todo_list.clear()
                

        print(f"\n{name}'s {listName} list")
        for key, value in todo_list.items():
            print(f"{key}: {value}")
        
        again = input('\n\nWould you like to continue updating your list?(y/n): ')
        if again.lower() == 'y':
           show_menu()
           choice = input('Enter the number that corresponds to your choice: ')

    else: 
        if again.lower() == 'n':
            print(f"\n{name}'s {listName} list")
            for key, value in todo_list.items():
                print(f"{key}: {value}")
        

except TypeError:
    print('Type in the number that corresponds to your choice')