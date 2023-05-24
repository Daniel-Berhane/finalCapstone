import os


def task_overview(t_list, date):
    """Generate file 'task_overview.txt' using data about the tasks."""
    # Collect the information from t_list
    # Use counters to count the completion details of the tasks
    # Loop through task list and check if completed == False and further checks due date hasn't gone past
    task_total = len(t_list)
    task_completed = 0
    task_uncompleted = 0
    task_uncompleted_overdue = 0
    for task in t_list:
        if task["completed"] == False:
            if task["due_date"].date() < date.today():
                task_uncompleted += 1
                task_uncompleted_overdue += 1
            else:
                task_uncompleted += 1
        else:
            task_completed += 1

    # Store incomplete tasks and overdue tasks in percentage format rounded to 2 decimal places
    # If the numbers are whole numbers then set them to integer 
    incomplete_percentage = round(((task_uncompleted / task_total) * 100), 2)
    if incomplete_percentage.is_integer():
        incomplete_percentage = int(incomplete_percentage)

    overdue_percentage = round(((task_uncompleted_overdue / task_total) * 100), 2)
    if overdue_percentage.is_integer():
        overdue_percentage = int(overdue_percentage)

    # Open 'task_overview.txt' in write mode and write the information to the .txt file
    with open('task_overview.txt', 'w') as t_overview:
        t_overview.write("__________Tasks Overview__________")
        t_overview.write(f"\n(Date modified: {str(date.today())})\n\n")
        t_overview.write(f"Total Tasks:        {task_total}")
        t_overview.write(f"\nTasks Completed:    {task_completed}")
        t_overview.write(f"\nTasks Incomplete:   {task_uncompleted}")
        t_overview.write(f"\nTasks Overdue:      {task_uncompleted_overdue}")
        t_overview.write(f"\n\nPercentage Incomplete:     {incomplete_percentage} %")
        t_overview.write(f"\nPercentage Overdue:        {overdue_percentage} %")


def user_overview(u_list, t_list, date):
    """Generate file 'user_overview.txt' using data about the users."""
    users_total = len(u_list)
    task_total = len(t_list)

    # Use write mode to create "user_overview.txt" and enter general data 
    with open('user_overview.txt', 'w') as u_overview:
        u_overview.write("__________Users Task Overview__________\n")
        u_overview.write(f"(Date modified: {str(date.today())})\n\n")
        u_overview.write(f"Total Users: {users_total}\n")
        u_overview.write(f"Total Tasks: {task_total}\n")

    # Loop through u_list to collect necessary data on each user
    # Create a new list of tasks assigned to that user
    # Work out how many tasks are assigned and what percentage of the total tasks this is
    for user in u_list:
        user_tasks = []
        for task in t_list:
            if task['username'] == user:
                user_tasks.append(task)
        total_user_tasks = len(user_tasks)
        percentage_tasks = round(((total_user_tasks / task_total) * 100), 2)
        if percentage_tasks.is_integer():
            percentage_tasks = int(percentage_tasks)

        # Use the user tasks list to work out how many tasks are complete, incomplete and overdue
        user_complete = 0
        user_incomplete = 0
        user_overdue = 0
        for task in user_tasks:
            if task['completed'] == True:
                user_complete += 1
            else:
                if task["due_date"].date() < date.today():
                    user_incomplete += 1
                    user_overdue += 1
                else:
                    user_incomplete += 1
        
        # Store complete, incomplete and overdue tasks in percentage format rounded to 2 decimal places
        # If the numbers are whole numbers then set them to integer 
        if user_complete != 0:
            user_complete_percentage = round(((user_complete / total_user_tasks) * 100), 2)
            if user_complete_percentage.is_integer():
                user_complete_percentage = int(user_complete_percentage)
        else:
            user_complete_percentage = 0

        if user_incomplete != 0:    
            user_incomplete_percentage = round(((user_incomplete / total_user_tasks) * 100), 2)
            if user_incomplete_percentage.is_integer():
                user_incomplete_percentage = int(user_incomplete_percentage)
        else:
            user_incomplete_percentage = 0

        if user_overdue != 0:
            user_overdue_percentage = round(((user_overdue / total_user_tasks) * 100), 2)
            if user_overdue_percentage.is_integer():
                user_overdue_percentage = int(user_overdue_percentage)
        else:
            user_overdue_percentage = 0
        
        # Use append mode to write the data for each user to 'user_overview.txt'
        # If the user has had no tasks assigned to them then write a message to file stating this
        with open('user_overview.txt', 'a') as u_overview:
            u_overview.write(f"\n-----\nUser: {user}\n\n")
            if total_user_tasks != 0:
                u_overview.write(f"Total number of tasks assigned:\t\t{total_user_tasks}\n")
                u_overview.write(f"Percentage of total tasks assigned:\t{percentage_tasks} %\n")
                u_overview.write(f"Percentage of tasks complete:\t\t{user_complete_percentage} %\n")
                u_overview.write(f"Percentage of tasks incomplete:\t\t{user_incomplete_percentage} %\n")
                u_overview.write(f"Percentage of tasks overdue:\t\t{user_overdue_percentage} %\n")
            else:
                u_overview.write("This user has not had any tasks assigned to them\n")


def display_statistics(t_list, u_list, date):
    """Output contents of 'task_overview.txt' and 'user_overview.txt' to the screen"""
    num_tasks = len(t_list)
    num_users = len(u_list)

    # Check if 'task_overview.txt' exists, if not creates the file using task_overview ()
    # Uses the data from 'task_overview.txt' and prints it on the screen in a user_friendly manner
    if not os.path.exists("task_overview.txt"):
        task_overview(t_list, date)
    
    with open('task_overview.txt','r') as t_overview:
        task_stats = t_overview.read().split("\n")
        del task_stats[0:4]


    print("\n----------Task Statistics----------\n")
    if num_users != 1:
        print(f"{num_tasks} tasks have been assigned to the user/s")  
    else:
        print(f"{num_tasks} task has been assigned to the user/s")
    print("Below is the task statistics:\n")
    print("\n".join(task_stats))
    print("\n-----------------------------------\n")

    # Check if 'user_overview.txt' exists, if not creates the file using user_overview ()
    # Uses the data from 'user_overview.txt' and prints it on the screen in a user_friendly manner
    if not os.path.exists("user_overview.txt"):
        user_overview(u_list, t_list, date)
    
    with open('user_overview.txt','r') as u_overview:
        user_stats = u_overview.read().split("\n")
        del user_stats[0:6]

    print("\n----------User Statistics----------\n")
    if num_users == 1:
        print(f"You have {num_users} user stored on the system.")
        print("Below is their stats:")
    else:
        print(f"You have {num_users} users stored on the system.")
        print("Below is each of their individual stats:\n")
    print("\n".join(user_stats))
    print("-----------------------------------\n")