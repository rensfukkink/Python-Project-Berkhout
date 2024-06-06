import os
import pyad.adquery
import logging

# Configureer logging
logging.basicConfig(filename='Migratie.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def create_share(username):
    share_path = f"\\\\SERVER01\\UserFolders\\{username}"

    # Controleer of de map al bestaat
    if not os.path.exists(share_path):
        # Maak de map aan
        os.makedirs(share_path)
        logging.info(f"Map voor gebruiker '{username}' aangemaakt op '{share_path}'.")

def check_and_create_shares_in_ou(ou_name, sub_ou_name, domain_name):
    # Verkrijg alle gebruikers in de OU
    query = pyad.adquery.ADQuery()
    query.execute_query(
        attributes=["cn"],
        where_clause=f"objectClass='user'",
        base_dn=f"OU={sub_ou_name},OU={ou_name},DC={domain_name.split('.')[0]},DC={domain_name.split('.')[1]}"
    )

    # Loop door elke gebruiker in de resultaten
    for row in query.get_results():
        username = row["cn"]

        # Controleer of de share van de gebruiker bestaat
        create_share(username)

if __name__ == "__main__":
    ou_name = "Berkhout-Users"
    sub_ou_name = "IT"
    domain_name = "Berkhout.local"
    check_and_create_shares_in_ou(ou_name, sub_ou_name, domain_name)
