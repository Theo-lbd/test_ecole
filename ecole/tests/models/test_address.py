from ecole.models.address import Address


def test_address_initialization():
    # Initialisation d'une adresse
    address = Address("12 rue des Pinsons", "Castanet", 31320)

    # Vérifie les attributs de l'adresse
    assert address.street == "12 rue des Pinsons"
    assert address.city == "Castanet"
    assert address.postal_code == 31320


def test_address_str():
    # Initialisation d'une adresse
    address = Address("12 rue des Pinsons", "Castanet", 31320)

    # Vérifie que la représentation en chaîne de caractères est correcte
    assert str(address) == "12 rue des Pinsons, 31320 Castanet"
