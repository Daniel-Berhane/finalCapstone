from datetime import datetime, date
from user import reg_user
from tasks import user_task, add_task, view_all, view_mine
from tasks_utilities import task_file_status, user_file_status, login_check, main_menu
from files_stats import task_overview, user_overview, display_statistics

DATETIME_STRING_FORMAT = "%Y-%m-%d"
DATE_STYLE = "YYYY-MM-DD"

task_list = task_file_status("tasks.txt", datetime, DATETIME_STRING_FORMAT)

username_password = user_file_status("user.txt", "admin;password")

# While loop used to check user login details are correct using .login_check()
# Provides access once details are verified
logged_in = False
while not logged_in:

    logged_in = login_check(username_password)

    if logged_in != False:
        curr_user = logged_in
        break

# Loop generates menu option until user selects exit option
# .main_menu() provides 2 options for user based on access status
while True:
    menu = main_menu(curr_user)

    # Based on menu choice a different function will be executed as listed below
    if menu == 'r':
        reg_user(username_password, "user.txt")

    elif menu == 'a':
        # user_task() returns a new task unless the user doesn't exist
        # If the user doesn't exist, false is returned
        new_task = user_task(username_password.keys(), datetime, date, DATE_STYLE, DATETIME_STRING_FORMAT)

        if new_task != False:
            task_list.append(new_task)
            add_task(task_list, "tasks.txt", DATETIME_STRING_FORMAT)
            print("\nTask successfully added")

    elif menu == 'va':
        view_all(task_list, DATETIME_STRING_FORMAT)
            
    elif menu == 'vm':
        view_mine(task_list, username_password.keys(), DATETIME_STRING_FORMAT, curr_user, datetime, date, "tasks.txt")

    elif menu == 'gr' and curr_user == "admin":
        task_overview(task_list, date)
        user_overview(username_password, task_list, date)
        print("\nYour files have been generated")

    # Function for 'ds' only executes if the user is an admin
    # If not an admin, the user receives a message informing them access is to admins only
    elif menu == 'ds' and curr_user == 'admin':
        display_statistics(task_list, username_password, date)

    elif menu == 'ds' and curr_user != 'admin':
        print("\nYou need to be an admin to access this feature\n")

    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    else:
        print("\nYou have made a wrong choice, Please Try again")