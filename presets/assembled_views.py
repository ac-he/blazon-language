# default_view = {
#     "w": 1600,
#     "h": 900,
#     "background": "mid-grey.png",
#     "crest-scale-width": 220,
#     "kerning": 30,
#     "line-spacing": 40,
#     "override-shapes": False,
#     "margin": 50,
#     "shapes": [
#         "rect"
#     ],
#     "crests": [
#
#     ]
# }

default_view = {
    "w": 3820,
    "h": 2100,
    "background": "bigmonitor-mid-grey.png",
    "crest-scale-width": 330,
    "kerning": 30,
    "line-spacing": 40,
    "override-shapes": False,
    "margin": 100,
    "shapes": [
        "rect"
    ],
    "crests": [

    ]
}

shapes = ["banner", "heater", "pennant", "rect", "shield"]

colors = ["g", "s", "v", "a", "p"]
metals = ["o", "r"]
charges = ["sun", "castle", "clarion"]
n = len(charges)


ci = 0
mi = 0
si = 0


def make_default_test_data(charge, quantity=1):
    global default_view, ci, mi

    charge_set = charge
    if charge == "mix":
        mix_default(quantity)
    elif isinstance(charge, str):
        charge_set = [charge]

    for stamp in charge_set:
        for shape in shapes:
            for quantity in range(1, quantity+1):
                default_view["crests"].append(add_per_bend(stamp, shape, quantity))
                default_view["crests"].append(add_per_bend_sinister(stamp, shape, quantity))
                default_view["crests"].append(add_per_chevron(stamp, shape, quantity))
                default_view["crests"].append(add_per_cross(stamp, shape, quantity))
                default_view["crests"].append(add_per_fess(stamp, shape, quantity))
                default_view["crests"].append(add_per_pale(stamp, shape, quantity))
                default_view["crests"].append(add_per_pall(stamp, shape, quantity))
                default_view["crests"].append(add_per_saltire(stamp, shape, quantity))

            mi = mi + 1
            ci = ci + 1


def mix_default(quantity=1):
    global default_view, ci, mi, si

    for shape in shapes:
        for quantity in range(1, quantity+1):
            default_view["crests"].append(add_per_bend(charges[si % n], shape, quantity))
            default_view["crests"].append(add_per_bend_sinister(charges[si % n], shape, quantity))
            default_view["crests"].append(add_per_chevron(charges[si % n], shape, quantity))
            default_view["crests"].append(add_per_cross(charges[si % n], shape, quantity))
            default_view["crests"].append(add_per_fess(charges[si % n], shape, quantity))
            default_view["crests"].append(add_per_pale(charges[si % n], shape, quantity))
            default_view["crests"].append(add_per_pall(charges[si % n], shape, quantity))
            default_view["crests"].append(add_per_saltire(charges[si % n], shape, quantity))

            si = si + 1

        mi = mi + 1
        ci = ci + 1


def make_default_test_data_by_division(division, charge, quantity=1):
    global default_view, ci, mi, si
    charge_set = charge
    if isinstance(charge, str):
        charge_set = [charge]

    for quantity in range(1, quantity + 1):
        for shape in shapes:
            for stamp in charge_set:
                match division:
                    case "per bend":
                        default_view["crests"].append(add_per_bend(stamp, shape, quantity))
                    case "per bend sinister":
                        default_view["crests"].append(add_per_bend_sinister(stamp, shape, quantity))
                    case "per bend both":
                        default_view["crests"].append(add_per_bend(stamp, shape, quantity))
                        default_view["crests"].append(add_per_bend_sinister(stamp, shape, quantity))
                    case "per chevron":
                        default_view["crests"].append(add_per_chevron(stamp, shape, quantity))
                    case "per cross":
                        default_view["crests"].append(add_per_cross(stamp, shape, quantity))
                    case "per fess":
                        default_view["crests"].append(add_per_fess(stamp, shape, quantity))
                    case "per pale":
                        default_view["crests"].append(add_per_pale(stamp, shape, quantity))
                    case "per pall":
                        default_view["crests"].append(add_per_pall(stamp, shape, quantity))
                    case "per saltire":
                        default_view["crests"].append(add_per_saltire(stamp, shape, quantity))

                mi = mi + 1
                ci = ci + 1


def add_per_bend(charge, shape, quantity):
    return {
        "shape": shape,
        "field": {
            "party": "per bend",
            "dexter-base": {
                "tincture": colors[ci % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "sinister-chief": {
                "tincture": metals[mi % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
        }
    }


def add_per_bend_sinister(charge, shape, quantity):
    return {
        "shape": shape,
        "field": {
            "party": "per bend sinister",
            "dexter-chief": {
                "tincture": colors[ci % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "sinister-base": {
                "tincture": metals[mi % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
        }
    }


def add_per_chevron(charge, shape, quantity):
    return {
        "shape": shape,
        "field": {
            "party": "per chevron",
            "chief": {
                "tincture": colors[ci % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "base": {
                "tincture": metals[mi % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
        }
    }


def add_per_cross(charge, shape, quantity):
    return {
        "shape": shape,
        "field": {
            "party": "per cross",
            "dexter-chief": {
                "tincture": colors[ci % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "sinister-base": {
                "tincture": colors[(ci + 1) % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "dexter-base": {
                "tincture": metals[(mi + 1) % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
            "sinister-chief": {
                "tincture": metals[mi % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
        }
    }


def add_per_fess(charge, shape, quantity):
    return {
        "shape": shape,
        "field": {
            "party": "per fess",
            "chief": {
                "tincture": colors[ci % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "base": {
                "tincture": metals[mi % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
        }
    }


def add_per_pale(charge, shape, quantity):
    return {
        "shape": shape,
        "field": {
            "party": "per pale",
            "dexter": {
                "tincture": colors[ci % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "sinister": {
                "tincture": metals[mi % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
        }
    }


def add_per_pall(charge, shape, quantity):
    return {
        "shape": shape,
        "field": {
            "party": "per pall",
            "dexter": {
                "tincture": colors[ci % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "sinister": {
                "tincture": colors[(ci+1) % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "chief": {
                "tincture": metals[mi % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
        }
    }


def add_per_saltire(charge, shape, quantity):
    return {
        "shape": shape,
        "field": {
            "party": "per saltire",
            "chief": {
                "tincture": colors[ci % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "dexter": {
                "tincture": metals[(mi + 1) % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
            "base": {
                "tincture": colors[(ci + 1) % 5],
                "charge": charge,
                "charge-tincture": metals[mi % 2],
                "quantity": quantity
            },
            "sinister": {
                "tincture": metals[mi % 2],
                "charge": charge,
                "charge-tincture": colors[ci % 5],
                "quantity": quantity
            },
        }
    }



