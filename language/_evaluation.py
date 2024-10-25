import math

charges = {
    "anchor": {"type": "cm", "value": 97},
    "annulet": {"type": "agoprsv", "value": 5},
    "bee": {"type": "cm", "value": 98},
    "billet": {"type": "agoprsv", "value": 2},
    "caltrap": {"type": "agoprsv", "value": 3},
    "castle": {"type": "cm", "value": 99},
    "chequy": {"type": "oversize", "value": 1000},
    "clarion": {"type": "cm", "value": 106},
    "comet": {"type": "cm", "value": 105},
    "crescent": {"type": "agoprsv", "value": 2},
    "cross_moline": {"type": "agoprsv", "value": 8},
    "cross_pate": {"type": "agoprsv", "value": 4},
    "crown": {"type": "cm", "value": 33},
    "dolphin": {"type": "cm", "value": 102},
    "dragon": {"type": "cm", "value": 100},
    "eagle": {"type": "cm", "value": 101},
    "escallop": {"type": "cm", "value": 46},
    "escutcheon": {"type": "agoprsv", "value": 9},
    "fleur_de_lis": {"type": "agoprsv", "value": 6},
    "fret": {"type": "oversize", "value": 1},
    "fusil": {"type": "agoprsv", "value": 5},
    "fusily": {"type": "oversize", "value": 1000},
    "gorge": {"type": "oversize", "value": 0},
    "griffin": {"type": "cm", "value": 103},
    "gyronny": {"type": "oversize", "value": -1},
    "harp": {"type": "cm", "value": 104},
    "keys": {"type": "cm", "value": 107},
    "label": {"type": "geo", "value": 1},
    "lamp": {"type": "cm", "value": 108},
    "lion_passant": {"type": "cm", "value": 32},
    "lion_rampant": {"type": "cm", "value": 10},
    "lozenge": {"type": "agoprsv", "value": 6},
    "lozengy": {"type": "oversize", "value": -1},
    "martlet": {"type": "agoprsv", "value": 4},
    "mascle": {"type": "agoprsv", "value": 7},
    "moon": {"type": "cm", "value": 109},
    "mullet": {"type": "agoprsv", "value": 3},
    "octofoil": {"type": "agoprsv", "value": 9},
    "owl": {"type": "cm", "value": 111},
    "phoenix": {"type": "cm", "value": 63},
    "portcullis": {"type": "cm", "value": 112},
    "quatrefoil": {"type": "cm", "value": 113},
    "quarterly_of_eight": {"type": "geo"},
    "raven": {"type": "cm", "value": 114},
    "rose": {"type": "agoprsv", "value": 7},
    "roundel": {"type": "agoprsv", "value": 0},
    "rustre": {"type": "agoprsv", "value": 8},
    "ship": {"type": "cm", "value": 115},
    "snairald": {"type": "cm"},
    "sun": {"type": "cm", "value": 110},
    "sword": {"type": "cm", "value": 120},
    "thistle": {"type": "cm", "value": 116},
    "unicorn": {"type": "cm", "value": 117},
    "ventmonster": {"type": "oversize"},
    "wheel": {"type": "cm", "value": 118},
    "wolf": {"type": "cm", "value": 119},
    "yale": {"type": "cm", "value": 121},
    "zilant": {"type": "cm", "value": 122},
}


def make_charge_render_friendly(charge):
    match charge:
        case "anchors": return "anchor"
        case "annulets": return "annulet"
        case "bees": return "bee"
        case "billets": return "billet"
        case "caltraps": return "caltrap"
        case "castles": return "castle"
        case "clarions": return "clarion"
        case "comets": return "comet"
        case "crescents": return "crescent"
        case "crossmoline": return "cross_moline"
        case "crossesmoline": return "cross_moline"
        case "crosspate": return "cross_pate"
        case "crossespate": return "cross_pate"
        case "crowns": return "crown"
        case "dolphins": return "dolphin"
        case "dragons": return "dragon"
        case "eagles": return "eagle"
        case "scallop": return "escallop"
        case "scallops": return "escallop"
        case "escutcheons": return "escutcheon"
        case "fleur-de-lis": return "fleur_de_lis"
        case "fleurs-de-lis": return "fleur_de_lis"
        case "fusils": return "fusil"
        case "griffins": return "griffin"
        case "harps": return "harp"
        case "setofkeyssaltirewise": return "keys"
        case "setsofkeyssaltirewise": return "keys"
        case "alabelof": return "label"
        case "lamps": return "lamp"
        case "lionpassant": return "lion_passant"
        case "lionspassant": return "lion_passant"
        case "lionrampant": return "lion_rampant"
        case "lionsrampant": return "lion_rampant"
        case "lozenges": return "lozenge"
        case "martlets": return "martlet"
        case "mascles": return "mascle"
        case "mooninherplenitude": return "moon"
        case "moonsintheirplenitude": return "moon"
        case "mullets": return "mullet"
        case "octofoils": return "octofoil"
        case "owls": return "owl"
        case "phoenixes": return "phoenix"
        case "portcullises": return "portcullis"
        case "quatrefoils": return "quatrefoil"
        case "quarterlyofeight": return "quarterly_of_eight"
        case "ravens": return "raven"
        case "roses": return "rose"
        case "roundels": return "roundel"
        case "rustres": return "rustre"
        case "ships": return "ship"
        case "suninhissplendor": return "sun"
        case "sunsintheirsplendor": return "sun"
        case "swords": return "sword"
        case "thistles": return "thistle"
        case "unicorns": return "unicorn"
        case "wheels": return "wheel"
        case "wolves": return "wolf"
        case "yales": return "yale"
        case "zilants": return "zilant"
        case _: return charge


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
    if s_charge == "quarterlyofeight":
        return interpret_quarterly_of_eight(field.charge_tincture)
    i_charge = charges[make_charge_render_friendly(s_charge)]["value"]

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
