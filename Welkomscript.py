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

        # Telefoonnummer van de servicedesk
        servicedesk_telefoonnummer = "123-456-789"

        # Bestandsnaam genereren
        bestandsnaam = f"{voornaam}_{achternaam}.txt"

        # Functie om alleen de groepsnaam en het directory pad te extraheren
        def extract_group_and_directory(group_dn):
            # Deel de DN op in delen gescheiden door komma's
            parts = group_dn.split(",")

            # Deel het eerste deel (CN=GroupName) verder op om alleen de groepsnaam te verkrijgen
            group_name = parts[0].split("=")[1]

            # Combineer de resterende delen om het directory pad te krijgen
            directory_path = ",".join(parts[1:])

            return group_name, directory_path

        # Gebruikersinformatie naar een tekstbestand schrijven
        with open(bestandsnaam, "w") as bestand:
            bestand.write(f"Welkom {gebruikersnaam}, dit zijn uw gegevens:\n")
            bestand.write(f"Voornaam: {voornaam}\n")
            bestand.write(f"Achternaam: {achternaam}\n")
            bestand.write(f"Weergavenaam: {weergavenaam}\n")
            bestand.write(f"E-mail: {e_mail}\n")
            bestand.write(f"Directory pad: \\\\Server01\\UserFolders\\{gebruikersnaam}\n")

            # Voor elke groep de naam extraheren en schrijven
            groep = gebruiker.get_attribute("memberOf") if gebruiker.get_attribute("memberOf") else ""
            for group_dn in groep:
                group_name, _ = extract_group_and_directory(group_dn)
                bestand.write(f"Groep: {group_name}\n")

            bestand.write(f"Telefoonnummer servicedesk: {servicedesk_telefoonnummer}\n")

        print(f"Gebruikersinformatie is geschreven naar {bestandsnaam}")
    else:
        print("Gebruiker niet gevonden in Active Directory.")


# Gegevens opvragen
if __name__ == "__main__":
    # Vraag de gebruiker om de gebruikersnaam om te zoeken
    gebruikersnaam = input("Voer de gebruikersnaam in om te zoeken: ")

    # Roep de zoek_gebruiker_en_schrijf_naar_bestand functie aan
    zoek_gebruiker_en_schrijf_naar_bestand(gebruikersnaam)




