import os
from pyad import *


def create_group(group_name):
    domain_name = "Berkhout.local"
    ou_name = "Berkhout-Groups"

    pyad.set_defaults(ldap_server=f"{domain_name}")

    ou_dn = f"OU={ou_name},{','.join(['DC=' + dc for dc in domain_name.split('.')])}"

    ou_container = pyad.adcontainer.ADContainer.from_dn(ou_dn)

    new_group = pyad.adgroup.ADGroup.create(group_name, ou_container)

    print("Group has been successfully created: ", new_group.get_attribute("cn"))

    return new_group


def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print("Directory has been successfully created: ", directory_path)
    else:
        print("Directory already exists: ", directory_path)


if __name__ == "__main__":
    group_name = input("Enter the name of the new group: ")
    directory_path = input("Enter the path for the new directory: ")

    new_group = create_group(group_name)
    create_directory(directory_path)