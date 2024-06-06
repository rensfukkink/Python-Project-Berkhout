import datetime
import logging
from pyad import pyad, aduser


def setup_logging():
    logging.basicConfig(filename='user_last_login.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging setup complete.")


def get_last_login(username):
    try:
        user = aduser.ADUser.from_cn(username)
        last_login = user.get_attribute("lastLogon")
        last_login_time = datetime.datetime.utcfromtimestamp(int(last_login) / 10000000 - 11644473600)
        return last_login_time
    except Exception as e:
        logging.error(f"Error retrieving last login time for user {username}: {e}")
        return None


def check_last_login(username, max_days=30):
    last_login_time = get_last_login(username)
    if last_login_time:
        current_time = datetime.datetime.utcnow()
        days_since_last_login = (current_time - last_login_time).days
        if days_since_last_login > max_days:
            print(f"WARNING: User '{username}' last logged in {days_since_last_login} days ago on {last_login_time}.")
            logging.warning(f"User '{username}' last logged in {days_since_last_login} days ago on {last_login_time}.")
        else:
            print(f"User '{username}' last logged in {days_since_last_login} days ago on {last_login_time}.")
            logging.info(f"User '{username}' last logged in {days_since_last_login} days ago on {last_login_time}.")
    else:
        print(f"Could not retrieve last login time for user '{username}'.")


if __name__ == "__main__":
    setup_logging()

    username = input("Enter username to check last login time: ")
    check_last_login(username)

