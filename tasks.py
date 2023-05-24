def user_task(names, date_time, date, date_style, date_formatted):
    """Create a new task dictionary using users input"""
    # Check if a user exists for a task to be assigned
    # If they don't exist return false
    username = input("\nName of person assigned to task: ")
    if username not in names:
        print("User does not exist. Please enter a valid username")
        return False
    else:
        # If user exists, collect remaining necessary information for task assignment
        # Check that a valid date format has been put in
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input(f"Due date of task ({date_style}): ")
                due_date_time = date_time.strptime(task_due_date, date_formatted)
                if due_date_time.date() < date.today():                  
                    print("This date cannot be set as it has already gone by")
                    continue
                break
            except ValueError:
                print("Invalid datetime format. Please use the format specified")

        # Then get the current date.
        curr_date = date.today()

        # Using the input details create a dictionary called new_task and return it
        new_task = {
            "username": username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        return new_task


def add_task(tasks, file, date_formatted):
    """Generate a file containing all the tasks and their information"""
    # Create a new empty list
    # Loop through each task and set up in a usable way then append to empty list
    task_list_to_write = []
    for t in tasks:
        str_attrs = [
            t['username'],
            t['title'],
            t['description'],
            t['due_date'].strftime(date_formatted),
            t['assigned_date'].strftime(date_formatted),
            "Yes" if t['completed'] else "No"
        ]

        task_list_to_write.append(";".join(str_attrs))
    
    # Open a file in write mode and add contents of task_list_to_write
    with open(file , "w") as task_file:
        task_file.write("\n".join(task_list_to_write))


def show_task(task, date_string):
    """Returns task data formatted to be more user_friendly"""
    disp_str = f"Task: \t\t\t {task['title']}\n"
    disp_str += f"Assigned to: \t\t {task['username']}\n"
    disp_str += f"Date Assigned: \t\t {task['assigned_date'].strftime(date_string)}\n"
    disp_str += f"Due Date: \t\t {task['due_date'].strftime(date_string)}\n"
    disp_str += f"Task Description: \t {task['description']}\n"
    return disp_str


def view_all(t_list, date_string):
    """Shows all tasks in the task list"""
    print()

    # If no tasks have been assigned, inform the user with the print statement
    if len(t_list) == 0:
        print("No tasks have been assigned")

    # Loop through t_list to access each task and use show_task() to display it in a readable way
    for t in t_list:
        current_task = show_task(t, date_string)
        print(current_task)


def view_mine(t_list, user_list, date_string, name, date_time, date, file):
    """Show the user all their task and provide options for marking the task complete and editing task assignment and due date"""
    # Provide user with a list of their tasks printed to the screen
    # Place the index number (in task list) and task into a seperate list
    print("\n____________________TASK LIST____________________\n")
    task_number = 1
    user_tasks = []
    for t in t_list:
        if t['username'] == name:
            list_index = t_list.index(t)
            task_with_index = [list_index, t]
            user_tasks.append(task_with_index)

            my_task = show_task(t, date_string)
            print(f"Task {task_number}")
            print("-------------------------------------------------")
            print(my_task, "\n")
            task_number += 1      
    
    if len(user_tasks) == 0:
        print("You have not had any tasks assigned to you\n")

    # If the user_tasks list is not empty let the user select which task to edit
    # They can enter -1 if they wish to return to the main menu
    if len(user_tasks) != 0:
        while True:
            task_id = int(input("Enter task number (-1 for main menu): "))
            if task_id < -1 or task_id > len(user_tasks) or task_id == 0:
                print("Sorry you have entered an invalid option")
                continue
            else:
                if task_id == -1:
                    return
                else:
                    while True:
                        # The user can choose whether to mark the task as complete or edit something else
                        task_id -= 1
                        mark_edit = input("\nEnter 'mark' to mark task as complete or 'edit' to edit the task: ").lower()
                        if mark_edit == "mark":
                            if user_tasks[task_id][1]["completed"] == False:
                                user_tasks[task_id][1]["completed"] = True
                                print("Your task is now marked as complete")
                            else:
                                print("This task has already been marked as complete")
                            break
                        # Provided option to edit due_date or username of the task if the task has not been completed
                        elif mark_edit == "edit":
                            if user_tasks[task_id][1]["completed"] == False:
                                # User can choose to edit who the task is assigned to
                                # Check to see that the user exists and if not then continues asking for another user
                                # If user exists, assign the task to them
                                while True:
                                    change_assigned = input("\nEdit assigned to (type 'y' for yes, 'n' for no): ").lower()
                                    if change_assigned == 'y':
                                        while True:
                                            new_assigned = input("Please enter the new user for task: ")
                                            if new_assigned not in user_list:
                                                print("This user has not been found")
                                                continue
                                            else:
                                                user_tasks[task_id][1]["username"] = new_assigned
                                                break
                                        break
                                    elif change_assigned != 'n':
                                        print("Invalid option")
                                        continue
                                    else:
                                        break
                                # User can choose to edit the due date of the task
                                # Check for a valid input to ensure that the date can be used
                                while True:
                                    change_due_date = input("\nEdit due date (type 'y' for yes, 'n' for no): ").lower()
                                    if change_due_date == 'y':
                                        while True:
                                            try:
                                                new_date = input("Update due date (YYYY-MM-DD): ")
                                                new_due_date = date_time.strptime(new_date, date_string)
                                                # If the new due date is in the past a message is printed informing them
                                                # Otherwise the date is updated with the new due date
                                                if new_due_date.date() >= date.today():
                                                    user_tasks[task_id][1]["due_date"] = new_due_date
                                                    break
                                                else:
                                                    print("This date cannot be set as it has already gone by")
                                                    continue
                                            except ValueError:
                                                print("Please use the specified date format (YYYY-MM-DD)")
                                        break
                                    elif change_due_date != 'n':
                                        print("Invalid option")
                                        continue
                                    else:
                                        break



                            else:
                                print("This task has already been completed")

                        # Continue looping until the user has entered a valid option
                        else:
                            print("\nSorry, you have entered an invalid option")
                            continue

                        
                        break
            
            # Edit the data in t_list using the index data in user_tasks and the new user_tasks
            task_index =user_tasks[task_id][0]
            t_list[task_index] = user_tasks[task_id][1]
            break
        

    add_task(t_list, file, date_string)