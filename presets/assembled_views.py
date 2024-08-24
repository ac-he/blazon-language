import random
from math import floor

import const

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
divisions = ["per bend", "per bend sinister", "per chevron", "per cross", "per fess", "per pale", "per pall",
             "per saltire"]

colors = ["g", "s", "v", "a", "p"]
metals = ["o", "r"]
all_tinctures = ["g", "s", "v", "a", "p", "o", "r"]

charges = []
for key in const.charges.keys():
    charges.append(key)

n = len(charges)


ci = 0
mi = 0
si = 0


def make_randomized_test_data(total, charge_list="all", shape_list="all", division_list="all",
                              quantity_list="all", quantity_frequencies="equal"):
    cl = charge_list
    if charge_list == "all":
        cl = charges

    sl = shape_list
    if shape_list == "all":
        sl = shapes

    dl = division_list
    if division_list == "all":
        dl = divisions

    ql = quantity_list
    if quantity_list == "all":
        ql = [1, 2, 3]

    qf = quantity_frequencies
    if quantity_frequencies == "equal":
        qf = [1, 1, 1]
    if len(quantity_frequencies) < len(quantity_list):
        qf.append(0)
        qf.append(0)

    wql = []
    for i in range(len(qf)):
        for j in range(qf[i]):
            wql.append(ql[i])

    for i in range(total):
        this_dl = dl[floor(random.random() * len(dl))]

        s = sl[floor(random.random() * len(sl))]

        a_rc = get_random_tincture_combo()
        a_cl = cl[floor(random.random() * len(cl))]
        a_ql = wql[floor(random.random() * len(wql))]

        b_rc = get_random_tincture_combo()
        b_cl = cl[floor(random.random() * len(cl))]
        b_ql = wql[floor(random.random() * len(wql))]

        c_rc = get_random_tincture_combo()
        c_cl = cl[floor(random.random() * len(cl))]
        c_ql = wql[floor(random.random() * len(wql))]

        d_rc = get_random_tincture_combo()
        d_cl = cl[floor(random.random() * len(cl))]
        d_ql = wql[floor(random.random() * len(wql))]

        if this_dl == "per bend":
            default_view["crests"].append(add_per_bend(
                [a_cl, b_cl],
                s,
                [a_ql, b_ql],
                tincture=[a_rc["field"], b_rc["field"]],
                c_tincture=[a_rc["charge"], b_rc["charge"]]
            ))
        elif this_dl == "per bend sinister":
            default_view["crests"].append(add_per_bend_sinister(
                [a_cl, b_cl],
                s,
                [a_ql, b_ql],
                tincture=[a_rc["field"], b_rc["field"]],
                c_tincture=[a_rc["charge"], b_rc["charge"]]
            ))
        elif this_dl == "per chevron":
            default_view["crests"].append(add_per_chevron(
                [a_cl, b_cl],
                s,
                [a_ql, b_ql],
                tincture=[a_rc["field"], b_rc["field"]],
                c_tincture=[a_rc["charge"], b_rc["charge"]]
            ))
        elif this_dl == "per cross":
            default_view["crests"].append(add_per_cross(
                [a_cl, b_cl, c_cl, d_cl],
                s,
                [a_ql, b_ql, c_ql, d_ql],
                tincture=[a_rc["field"], b_rc["field"], c_rc["field"], d_rc["field"]],
                c_tincture=[a_rc["charge"], b_rc["charge"], c_rc["charge"], d_rc["charge"]]
            ))
        elif this_dl == "per fess":
            default_view["crests"].append(add_per_fess(
                [a_cl, b_cl],
                s,
                [a_ql, b_ql],
                tincture=[a_rc["field"], b_rc["field"]],
                c_tincture=[a_rc["charge"], b_rc["charge"]]
            ))
        elif this_dl == "per pale":
            default_view["crests"].append(add_per_pale(
                [a_cl, b_cl],
                s,
                [a_ql, b_ql],
                tincture=[a_rc["field"], b_rc["field"]],
                c_tincture=[a_rc["charge"], b_rc["charge"]]
            ))
        elif this_dl == "per pall":
            default_view["crests"].append(add_per_pall(
                [a_cl, b_cl, c_cl],
                s,
                [a_ql, b_ql, c_ql],
                tincture=[a_rc["field"], b_rc["field"], c_rc["field"]],
                c_tincture=[a_rc["charge"], b_rc["charge"], c_rc["charge"]]
            ))
        elif this_dl == "per saltire":
            default_view["crests"].append(add_per_saltire(
                [a_cl, b_cl, c_cl, d_cl],
                s,
                [a_ql, b_ql, c_ql, d_ql],
                tincture=[a_rc["field"], b_rc["field"], c_rc["field"], d_rc["field"]],
                c_tincture=[a_rc["charge"], b_rc["charge"], c_rc["charge"], d_rc["charge"]]
            ))


def get_random_tincture_combo():
    m = metals[floor(random.random() * 2)]
    c = colors[floor(random.random() * 5)]

    metal_field = random.random() > 0.5
    if metal_field:
        return {"field": m, "charge": c}
    else:
        return {"field": c, "charge": m}


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


def expand_defaults(charge, quantity, tincture, c_tincture):
    if not isinstance(charge, list):
        add_charges = [charge, charge, charge, charge]
    else:
        add_charges = charge

    if not isinstance(quantity, list):
        add_quantities = [quantity, quantity, quantity, quantity]
    else:
        add_quantities = quantity

    if not isinstance(tincture, list):
        add_tinctures = [colors[ci % 5], metals[mi % 2], colors[ci % 5], metals[mi % 2]]
    else:
        add_tinctures = tincture

    if not isinstance(c_tincture, list):
        add_c_tinctures = [metals[mi % 2], colors[ci % 5], metals[mi % 2], colors[ci % 5]]
    else:
        add_c_tinctures = c_tincture

    return {
        "charges": add_charges,
        "quantities": add_quantities,
        "tinctures": add_tinctures,
        "c-tinctures": add_c_tinctures
    }


def add_per_bend(charge, shape, quantity, tincture="preset", c_tincture="preset"):
    settings = expand_defaults(charge, quantity, tincture=tincture, c_tincture=c_tincture)

    return {
        "shape": shape,
        "field": {
            "party": "per bend",
            "dexter-base": {
                "tincture": settings["tinctures"][0],
                "charge": settings["charges"][0],
                "charge-tincture": settings["c-tinctures"][0],
                "quantity": settings["quantities"][0]
            },
            "sinister-chief": {
                "tincture": settings["tinctures"][1],
                "charge": settings["charges"][1],
                "charge-tincture": settings["c-tinctures"][1],
                "quantity": settings["quantities"][1]
            },
        }
    }


def add_per_bend_sinister(charge, shape, quantity, tincture="preset", c_tincture="preset"):
    settings = expand_defaults(charge, quantity, tincture=tincture, c_tincture=c_tincture)

    return {
        "shape": shape,
        "field": {
            "party": "per bend sinister",
            "dexter-chief": {
                "tincture": settings["tinctures"][0],
                "charge": settings["charges"][0],
                "charge-tincture": settings["c-tinctures"][0],
                "quantity": settings["quantities"][0]
            },
            "sinister-base": {
                "tincture": settings["tinctures"][1],
                "charge": settings["charges"][1],
                "charge-tincture": settings["c-tinctures"][1],
                "quantity": settings["quantities"][1]
            },
        }
    }


def add_per_chevron(charge, shape, quantity,  tincture="preset", c_tincture="preset"):
    settings = expand_defaults(charge, quantity, tincture=tincture, c_tincture=c_tincture)

    return {
        "shape": shape,
        "field": {
            "party": "per chevron",
            "chief": {
                "tincture": settings["tinctures"][0],
                "charge": settings["charges"][0],
                "charge-tincture": settings["c-tinctures"][0],
                "quantity": settings["quantities"][0]
            },
            "base": {
                "tincture": settings["tinctures"][1],
                "charge": settings["charges"][1],
                "charge-tincture": settings["c-tinctures"][1],
                "quantity": settings["quantities"][1]
            },
        }
    }


def add_per_cross(charge, shape, quantity,  tincture="preset", c_tincture="preset"):
    settings = expand_defaults(charge, quantity, tincture=tincture, c_tincture=c_tincture)

    return {
        "shape": shape,
        "field": {
            "party": "per cross",
            "dexter-chief": {
                "tincture": settings["tinctures"][0],
                "charge": settings["charges"][0],
                "charge-tincture": settings["c-tinctures"][0],
                "quantity": settings["quantities"][0]
            },
            "sinister-base": {
                "tincture": settings["tinctures"][1],
                "charge": settings["charges"][1],
                "charge-tincture": settings["c-tinctures"][1],
                "quantity": settings["quantities"][1]
            },
            "dexter-base": {
                "tincture": settings["tinctures"][2],
                "charge": settings["charges"][2],
                "charge-tincture": settings["c-tinctures"][2],
                "quantity": settings["quantities"][2]
            },
            "sinister-chief": {
                "tincture": settings["tinctures"][3],
                "charge": settings["charges"][3],
                "charge-tincture": settings["c-tinctures"][3],
                "quantity": settings["quantities"][3]
            },
        }
    }


def add_per_fess(charge, shape, quantity,  tincture="preset", c_tincture="preset"):
    settings = expand_defaults(charge, quantity, tincture=tincture, c_tincture=c_tincture)

    return {
        "shape": shape,
        "field": {
            "party": "per fess",
            "chief": {
                "tincture": settings["tinctures"][0],
                "charge": settings["charges"][0],
                "charge-tincture": settings["c-tinctures"][0],
                "quantity": settings["quantities"][0]
            },
            "base": {
                "tincture": settings["tinctures"][1],
                "charge": settings["charges"][1],
                "charge-tincture": settings["c-tinctures"][1],
                "quantity": settings["quantities"][1]
            },
        }
    }


def add_per_pale(charge, shape, quantity,  tincture="preset", c_tincture="preset"):
    settings = expand_defaults(charge, quantity, tincture=tincture, c_tincture=c_tincture)

    return {
        "shape": shape,
        "field": {
            "party": "per pale",
            "dexter": {
                "tincture": settings["tinctures"][0],
                "charge": settings["charges"][0],
                "charge-tincture": settings["c-tinctures"][0],
                "quantity": settings["quantities"][0]
            },
            "sinister": {
                "tincture": settings["tinctures"][1],
                "charge": settings["charges"][1],
                "charge-tincture": settings["c-tinctures"][1],
                "quantity": settings["quantities"][1]
            },
        }
    }


def add_per_pall(charge, shape, quantity,  tincture="preset", c_tincture="preset"):
    settings = expand_defaults(charge, quantity, tincture=tincture, c_tincture=c_tincture)

    return {
        "shape": shape,
        "field": {
            "party": "per pall",
            "dexter": {
                "tincture": settings["tinctures"][0],
                "charge": settings["charges"][0],
                "charge-tincture": settings["c-tinctures"][0],
                "quantity": settings["quantities"][0]
            },
            "sinister": {
                "tincture": settings["tinctures"][1],
                "charge": settings["charges"][1],
                "charge-tincture": settings["c-tinctures"][1],
                "quantity": settings["quantities"][1]
            },
            "chief": {
                "tincture": settings["tinctures"][2],
                "charge": settings["charges"][2],
                "charge-tincture": settings["c-tinctures"][2],
                "quantity": settings["quantities"][2]
            },
        }
    }


def add_per_saltire(charge, shape, quantity,  tincture="preset", c_tincture="preset"):
    settings = expand_defaults(charge, quantity, tincture=tincture, c_tincture=c_tincture)

    return {
        "shape": shape,
        "field": {
            "party": "per saltire",
            "chief": {
                "tincture": settings["tinctures"][0],
                "charge": settings["charges"][0],
                "charge-tincture": settings["c-tinctures"][0],
                "quantity": settings["quantities"][0]
            },
            "dexter": {
                "tincture": settings["tinctures"][1],
                "charge": settings["charges"][1],
                "charge-tincture": settings["c-tinctures"][1],
                "quantity": settings["quantities"][1]
            },
            "base": {
                "tincture": settings["tinctures"][2],
                "charge": settings["charges"][2],
                "charge-tincture": settings["c-tinctures"][2],
                "quantity": settings["quantities"][2]
            },
            "sinister": {
                "tincture": settings["tinctures"][3],
                "charge": settings["charges"][3],
                "charge-tincture": settings["c-tinctures"][3],
                "quantity": settings["quantities"][3]
            },
        }
    }
