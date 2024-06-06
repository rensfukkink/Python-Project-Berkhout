from pyad import *


# Functie om gebruikers in Active Directory te zoeken en hun informatie naar een tekstbestand te schrijven
def zoek_gebruiker_en_schrijf_naar_bestand(gebruikersnaam):
    gebruiker = pyad.aduser.ADUser.from_cn(gebruikersnaam)
    if gebruiker:
        # Gebruikersinformatie extraheren
        gebruikersnaam = gebruiker.get_attribute("samAccountName")[0] if gebruiker.get_attribute(
            "samAccountName") else ""
        voornaam = gebruiker.get_attribute("givenName")[0] if gebruiker.get_attribute("givenName") else ""
        achternaam = gebruiker.get_attribute("sn")[0] if gebruiker.get_attribute("sn") else ""
        weergavenaam = gebruiker.get_attribute("displayName")[0] if gebruiker.get_attribute("displayName") else ""
        e_mail = gebruiker.get_attribute("mail")[0] if gebruiker.get_attribute("mail") else ""
        phone_number = gebruiker.get_attribute("telephoneNumber")[0] if gebruiker.get_attribute("telephoneNumber") else ""
        office = gebruiker.get_attribute("physicalDeliveryOfficeName")[0] if gebruiker.get_attribute("physicalDeliveryOfficeName") else ""
        room = gebruiker.get_attribute("roomNumber")[0] if gebruiker.get_attribute("roomNumber") else ""
        title = gebruiker.get_attribute("title")[0] if gebruiker.get_attribute("title") else ""

        # Bestandsnaam genereren
        bestandsnaam = f"{voornaam}_{achternaam}.txt"

        # Gebruikersinformatie naar een tekstbestand schrijven
        with open(bestandsnaam, "w") as bestand:
            bestand.write("Gebruikersinformatie:\n")
            bestand.write(f"Gebruikersnaam: {gebruikersnaam}\n")
            bestand.write(f"Voornaam: {voornaam}\n")
            bestand.write(f"Achternaam: {achternaam}\n")
            bestand.write(f"Weergavenaam: {weergavenaam}\n")
            bestand.write(f"E-mail: {e_mail}\n")
            bestand.write(f"Telefoonnummer: {phone_number}\n")
            bestand.write(f"Kantoor: {office}\n")
            bestand.write(f"Kamer: {room}\n")
            bestand.write(f"Titel: {title}\n")

        print(f"Gebruikersinformatie is geschreven naar {bestandsnaam}")
    else:
        print("Gebruiker niet gevonden in Active Directory.")


# Gegevens opvragen
if __name__ == "__main__":
    # Vraag de gebruiker om de gebruikersnaam om te zoeken
    gebruikersnaam = input("Voer de gebruikersnaam in om te zoeken: ")

    # Roep de zoek_gebruiker_en_schrijf_naar_bestand functie aan
    zoek_gebruiker_en_schrijf_naar_bestand(gebruikersnaam)