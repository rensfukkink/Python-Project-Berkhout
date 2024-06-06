import os
import subprocess
import logging
from pyad import pyad, aduser, adcontainer


def setup_logging():
    logging.basicConfig(filename='user_creation.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging setup complete.")


def add_user(username, password, first_name, last_name):
    domain_name = "Berkhout.local"
    ou_name = "Berkhout-Users"
    sub_ou_name = "IT"

    pyad.set_defaults(ldap_server=f"{domain_name}")

    try:
        sub_ou_dn = f"OU={sub_ou_name},{','.join(['OU=' + ou for ou in ou_name.split('.')])},{','.join(['DC=' + dc for dc in domain_name.split('.')])}"
        sub_ou_container = adcontainer.ADContainer.from_dn(sub_ou_dn)

        new_user = aduser.ADUser.create(username, sub_ou_container)
        new_user.set_password(password)
        new_user.update_attributes({
            "givenName": first_name,
            "sn": last_name,
            "displayName": f"{first_name} {last_name}",
            "userPrincipalName": f"{username}@{domain_name}",
            "profilePath": f"\\\\SERVER01\\UserProfiles\\{username}",
            "homeDirectory": f"\\\\SERVER01\\UserFolders\\{username}",
            "homeDrive": "H:"
        })

        logging.info(f"User {username} has been successfully added.")
        logging.info(f"Profile path: \\\\SERVER01\\UserProfiles\\{username}")
        logging.info(f"Home folder: \\\\SERVER01\\UserFolders\\{username}")

        print("User has been successfully added.")
        return new_user

    except Exception as e:
        logging.error(f"Error adding user {username}: {e}")
        print(f"Error adding user: {e}")
        return None


if __name__ == "__main__":
    setup_logging()

    username = input("Username: ")
    password = input("Password: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    add_user(username, password, first_name, last_name)


    def log_actie(actie):
        try:
            logging.info(actie)
        except Exception as e:
            logging.error(f"Error logging action: {e}")