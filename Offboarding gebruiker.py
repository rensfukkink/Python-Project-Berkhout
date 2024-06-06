import os
import shutil
import logging

def setup_logging():
    logging.basicConfig(filename='Offboarding.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging setup complete.")

def move_user_directory(username):
    user_directory = f"\\\\Server01\\UserFolders\\{username}"
    backup_directory = f"B:\\UserBackup\\{username}"
    if os.path.exists(user_directory):
        shutil.move(user_directory, backup_directory)
        logging.info(f"User '{username}' directory moved to backup directory.")
        print(f"User '{username}' directory moved to backup directory.")
    else:
        logging.warning(f"User '{username}' directory does not exist.")
        print(f"User '{username}' directory does not exist.")

if __name__ == "__main__":
    setup_logging()

    username = input("Enter username: ")

    move_user_directory(username)
