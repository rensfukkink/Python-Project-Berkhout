from pyad import *
from datetime import *
import random
import string

# Functie om een veilig wachtwoord te genereren
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Functie om de laatste login tijd op te halen
def get_last_logon(user):
    # Haal de lastLogonTimestamp op en converteer deze naar een leesbaar formaat
    last_logon_timestamp = user.get_attribute("lastLogonTimestamp")
    if last_logon_timestamp:
        last_logon_datetime = datetime.fromtimestamp(int(last_logon_timestamp) / 10000000 - 11644473600)
        return last_logon_datetime
    return None

# Functie om een waarschuwing te geven en om actie te vragen
def check_last_logon_and_warn(username, max_days=30):
    try:
        # Vind de gebruiker in AD
        user = aduser.ADUser.from_cn(username)
    except Exception as e:
        print(f"Error finding user {username}: {e}")
        return

    last_logon = get_last_logon(user)
    if last_logon:
        days_since_last_logon = (datetime.now() - last_logon).days
        if days_since_last_logon > max_days:
            print(f"Warning: User {user.get_attribute('cn')} has not logged in for {days_since_last_logon} days.")
            action = input("Do you want to reset the password (r) or disable the account (d)? (r/d): ")
            if action.lower() == 'r':
                new_password = generate_password()
                user.set_password(new_password)
                print(f"Password for user {user.get_attribute('cn')} has been reset to: {new_password}")
            elif action.lower() == 'd':
                user.disable()
                print(f"User {user.get_attribute('cn')} has been disabled.")
    else:
        print(f"User {user.get_attribute('cn')} has never logged in or lastLogonTimestamp is not set.")

if __name__ == "__main__":
   username = input("Enter the username to check last logon: ")
    check_last_logon_and_warn(username)
