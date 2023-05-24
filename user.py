def username_check(names_list):
    """Check if username is stored in a username list"""
    # Loop to check if the new_username is in a list provided
    # If username is in the list continue asking for a new username, f not return the given username
    in_use = True
    while in_use:
        in_use = False
        new_username = input("\nNew Username: ")
        for user in names_list:
            if new_username == user:
                print("Sorry this username is already in use")
                in_use = True
                break
            
    return new_username


def password_check():
    """Gets a user to put in and confirm a password"""
    # User inputs two sets of passwords and the loop will continue until they've provided a matching pair
    while True:
        new_password = input("\nEnter password: ")
        confirm_password = input("Confirm password: ")

        if new_password == confirm_password:
            return new_password
        else:
            print("Passwords do not match")
            continue


def reg_user(user_list, file):
    """Register a user name and password to a file."""
    # Username_check() and password_check provide the necessary details for username and password
    # The user_list is updated with the new details
    username = username_check(user_list.keys())
    password = password_check()
    user_list[username] = password

    # New list is created in a format for the output file and written to the file 
    user_data= []
    for user in user_list:
        user_data.append(f"{user};{user_list[user]}")

    with open(file, "w") as user_file: 
        user_file.write("\n".join(user_data))