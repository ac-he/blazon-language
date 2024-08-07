default_view = {
    "w": 1600,
    "h": 900,
    "background": "mid-grey.png",
    "crest-scale-width": 220,
    "kerning": 30,
    "line-spacing": 40,
    "override-shapes": False,
    "margin": 50,
    "shapes": [
        "rect"
    ],
    "crests": [

    ]
}

shapes = ["rect", "banner", "pennant", "shield", "heater"]

colors = ["g", "s", "v", "a", "p"]
metals = ["o", "r"]
ci = 0
mi = 0


def make_default_test_data(charge):
    global default_view, ci, mi

    for shape in shapes:
        for quantity in range(1, 4):
            default_view["crests"].append(add_per_bend(charge, shape, quantity))
            default_view["crests"].append(add_per_bend_sinister(charge, shape, quantity))
            default_view["crests"].append(add_per_chevron(charge, shape, quantity))
            default_view["crests"].append(add_per_cross(charge, shape, quantity))
            default_view["crests"].append(add_per_fess(charge, shape, quantity))
            default_view["crests"].append(add_per_pale(charge, shape, quantity))
            default_view["crests"].append(add_per_pall(charge, shape, quantity))
            default_view["crests"].append(add_per_saltire(charge, shape, quantity))

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



