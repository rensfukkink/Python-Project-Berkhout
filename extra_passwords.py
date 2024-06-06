from pyad import *
import random
import string

# Functie om een veilig wachtwoord te genereren
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def add_user(username, first_name, last_name):
    domain_name = "Berkhout.local"
    ou_name = "Berkhout-Users"
    sub_ou_name = "IT"

    # Construct the DN for the sub OU
    sub_ou_dn = f"OU={sub_ou_name},OU={ou_name},DC={domain_name.replace('.', ',DC=')}"

    # Create the sub OU container object
    sub_ou_container = adcontainer.ADContainer.from_dn(sub_ou_dn)

    # Generate a password for the new user
    password = generate_password()

    # Create the new user
    new_user = aduser.ADUser.create(username, sub_ou_container, password=password)

    # Set user attributes
    new_user.update_attribute("givenName", first_name)
    new_user.update_attribute("sn", last_name)
    new_user.update_attribute("displayName", f"{first_name} {last_name}")
    new_user.update_attribute("userPrincipalName", f"{username}@{domain_name}")

    # Set the profile path
    user_profile_path = fr"\\SERVER01\UserProfiles\{username}"
    new_user.update_attribute("profilePath", user_profile_path)
    print("Profile path has been successfully set: ", user_profile_path)

    # Set the home folder
    user_home_folder = fr"\\SERVER01\UserFolders\{username}"
    new_user.update_attribute("homeDirectory", user_home_folder)
    new_user.update_attribute("homeDrive", "H:")
    print("Home folder has been successfully set: ", user_home_folder)

    print("User has been successfully added: ", new_user.get_attribute("cn"))

    # Save the username and password to a file
    with open("new_users.txt", "a") as file:
        file.write(f"{username}:  {password}\n")

    return new_user


if __name__ == "__main__":
    username = input("Username: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    add_user(username, first_name, last_name)