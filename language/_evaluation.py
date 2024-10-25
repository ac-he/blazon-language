import math

charge_values = {
    "anchor": 97,
    "anchors": 97,
    "annulet": 5,
    "annulets": 5,
    "bee": 98,
    "bees": 98,
    "billet": 2,
    "billets": 2,
    "caltrap": 3,
    "caltraps": 3,
    "castle": 99,
    "castles": 99,
    "chequy": 1000,
    "clarion": 106,
    "clarions": 106,
    "comet": 105,
    "comets": 105,
    "crescent": 2,
    "crescents": 2,
    "crossmoline": 8,
    "crossesmoline": 8,
    "crosspate": 4,
    "crossespate": 4,
    "crown": 33,
    "crowns": 33,
    "dolphin": 102,
    "dolphins": 102,
    "dragon": 100,
    "dragons": 100,
    "eagle": 101,
    "eagles": 101,
    "scallop": 46,
    "scallops": 46,
    "escutcheon": 9,
    "escutcheons": 9,
    "fleur-de-lis": 6,
    "fleurs-de-lis": 6,
    "fret": 1,
    "fusil": 5,
    "fusils": 5,
    "fusily": 1000,
    "gorge": 0,
    "griffin": 103,
    "griffins": 103,
    "gyronny": -1,
    "harp": 104,
    "harps": 104,
    "setofkeyssaltirewise": 107,
    "setsofkeyssaltirewise": 107,
    "alabelof": 1,
    "lamp": 108,
    "lamps": 108,
    "lionpassant": 32,
    "lionspassant": 32,
    "lionrampant": 10,
    "lionsrampant": 10,
    "lozenge": 6,
    "lozenges": 6,
    "lozengy": -1,
    "martlet": 4,
    "martlets": 4,
    "mascle": 7,
    "mascles": 7,
    "mooninherplenitude": 109,
    "moonsintheirplenitude": 109,
    "mullet": 3,
    "mullets": 3,
    "octofoil": 9,
    "octofoils": 9,
    "owl": 111,
    "owls": 111,
    "phoenix": 63,
    "phoenixes": 63,
    "portcullis": 112,
    "portcullises": 112,
    "quatrefoil": 113,
    "quatrefoils": 113,
    "raven": 114,
    "ravens": 114,
    "rose": 7,
    "roses": 7,
    "roundel": 0,
    "roundels": 0,
    "rustre": 8,
    "rustres": 8,
    "ship": 115,
    "ships": 115,
    "suninhissplendor": 110,
    "sunsintheirsplendor": 110,
    "sword": 120,
    "swords": 120,
    "thistle": 116,
    "thistles": 116,
    "unicorn": 117,
    "unicorns": 117,
    "wheel": 118,
    "wheels": 118,
    "wolf": 119,
    "wolves": 119,
    "yale": 121,
    "yales": 121,
    "zilant": 122,
    "zilants": 122
}


def stringify_charge(charge):
    return "".join(charge)


def integerify_quantity(quantity):
    if isinstance(quantity, list):
        quantity = quantity[0]

    match quantity:
        case "a":
            return 1
        case "an":
            return 1
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3


def get_int_value(field):
    s_charge = stringify_charge(field.charge)
    i_charge = charge_values.get(s_charge)

    if s_charge == "quarterlyofeight":
        return interpret_quarterly_of_eight(field.charge_tincture)

    if field.charge_quantity:
        i_quantity = integerify_quantity(field.charge_quantity)
    else:
        i_quantity = 1

    return int(math.pow(i_charge, i_quantity))


def interpret_quarterly_of_eight(tinctures):
    total = 0
    for i in range(8):
        tincture = tinctures[i * 2]

        if not is_metal(tincture):
            total += math.pow(2, 7 - i)

    return int(total)


def is_metal(tincture):
    if tincture == "argent" or tincture == "or":
        return True
    return False


def get_operator_string(field):
    match field.field_tincture:
        case "argent": return "Add", "to"
        case "or": return "Subtract", "from"
        case "sable": return "Multiply", "by"
        case "gules": return "Divide", "by"
        case "purpure": return "Mod", "by"
        case "azure": return "Raise", "to the power of"
        case "vert": return "root", None


def get_comparison(field):
    match field.field_tincture:
        case "argent": return "less than"
        case "or": return "greater than"
        case "sable": return "equal to"
        case "gules": return "not equal to"
        case "purpure": return "less than or equal to"
        case "azure": return "greater than or equal to"
        case "vert": return "equal to"
