tinctures = {
    "r": {"r": 243/255, "g": 243/255, "b": 243/255, "fullname": "argent", "type": "metal"},
    "o": {"r": 241/255, "g": 194/255, "b": 50/255, "fullname": "or", "type": "metal"},
    "g": {"r": 190/255, "g": 37/255, "b": 37/255, "fullname": "gules", "type": "colour"},
    "v": {"r": 78/255, "g": 111/255, "b": 52/255, "fullname": "vert", "type": "colour"},
    "a": {"r": 17/255, "g": 85/255, "b": 204/255, "fullname": "azure", "type": "colour"},
    "s": {"r": 22/255, "g": 22/255, "b": 22/255, "fullname": "sable", "type": "colour"},
    "p": {"r": 130/255, "g": 77/255, "b": 121/255, "fullname": "purpure", "type": "colour"},
}

canvas = {
    "w": 600,
    "h": 800
}

charge_size = {
    "f": 512,  # full
    "l": canvas["w"] * 0.4,  # large
    "m": canvas["w"] * 0.3,  # medium
    "s": canvas["w"] * 0.2,   # small
    "xs": canvas["w"] * 0.15     # x small
}

charge_loc = {
    "per bend": {
        "dexter-base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.450]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.275, canvas["w"] * 0.100],
                    "loc_y": [canvas["h"] * 0.325, canvas["h"] * 0.500, canvas["h"] * 0.675]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.1],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.650]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.275, canvas["w"] * 0.450],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.550, canvas["h"] * 0.725]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.4]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.275, canvas["w"] * 0.375],
                    "loc_y": [canvas["h"] * 0.325, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.205, canvas["w"] * 0.315, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.275, canvas["h"] * 0.475, canvas["h"] * 0.675]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.600]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.450, canvas["h"] * 0.700]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.025, canvas["w"] * 0.375],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.700, canvas["h"] * 0.700]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.1],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.05, canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.65]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.250, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.355, canvas["h"] * 0.530, canvas["h"] * 0.705]
                }
            }
        },
        "sinister-chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.45],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.325, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.675, canvas["w"] * 0.675, canvas["w"] * 0.325],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.45],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.675, canvas["w"] * 0.675, canvas["w"] * 0.325],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.350, canvas["w"] * 0.585],
                    "loc_y": [canvas["h"] * 0.040, canvas["h"] * 0.040]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.350, canvas["w"] * 0.575, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.040, canvas["h"] * 0.210, canvas["h"] * 0.040]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.45],
                    "loc_y": [canvas["h"] * 0.15]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.675, canvas["w"] * 0.675, canvas["w"] * 0.325],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.45],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.675, canvas["w"] * 0.675, canvas["w"] * 0.325],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            }
        }
    },
    "per bend sinister": {
        "dexter-chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.325, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.025, canvas["w"] * 0.375],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.100]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.025, canvas["w"] * 0.375],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.200],
                    "loc_y": [canvas["h"] * 0.100]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.450, canvas["w"] * 0.215],
                    "loc_y": [canvas["h"] * 0.040, canvas["h"] * 0.040]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.450, canvas["w"] * 0.225, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.040, canvas["h"] * 0.210, canvas["h"] * 0.040]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.150]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.025, canvas["w"] * 0.375],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.100]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.025, canvas["w"] * 0.375],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            }
        },
        "sinister-base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.450]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.700, canvas["w"] * 0.525, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.325, canvas["h"] * 0.500, canvas["h"] * 0.675]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.500],
                    "loc_y": [canvas["h"] * 0.500]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.650]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.700, canvas["w"] * 0.525, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.550, canvas["h"] * 0.725]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.400]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.525, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.325, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.645, canvas["w"] * 0.535, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.275, canvas["h"] * 0.475, canvas["h"] * 0.675]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.450],
                    "loc_y": [canvas["h"] * 0.600]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.450, canvas["h"] * 0.700]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.675, canvas["w"] * 0.675, canvas["w"] * 0.325],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.700, canvas["h"] * 0.700]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.500],
                    "loc_y": [canvas["h"] * 0.500]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.650]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.550, canvas["w"] * 0.375],
                    "loc_y": [canvas["h"] * 0.355, canvas["h"] * 0.530, canvas["h"] * 0.705]
                }
            }
        },
    },
    "per chevron": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.055]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.150, canvas["h"] * 0.050, canvas["h"] * 0.150]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.100, canvas["h"] * 0.200]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.180, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.080, canvas["h"] * 0.080]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.210, canvas["h"] * 0.050, canvas["h"] * 0.210]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.100, canvas["h"] * 0.200]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.055]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.150, canvas["h"] * 0.050, canvas["h"] * 0.150]
                }
            }
        },
        "base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.425]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.525, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.600, canvas["h"] * 0.490, canvas["h"] * 0.600]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.55]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.157, canvas["w"] * 0.525],
                    "loc_y": [canvas["h"] * 0.600, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.175, canvas["w"] * 0.350, canvas["w"] * 0.525],
                    "loc_y": [canvas["h"] * 0.675, canvas["h"] * 0.460, canvas["h"] * 0.675]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.320, canvas["w"] * 0.425, canvas["w"] * 0.530],
                    "loc_y": [canvas["h"] * 0.470, canvas["h"] * 0.610, canvas["h"] * 0.470]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.6]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.600, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.125, canvas["w"] * 0.350, canvas["w"] * 0.570],
                    "loc_y": [canvas["h"] * 0.725, canvas["h"] * 0.475, canvas["h"] * 0.725]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.500]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.175, canvas["w"] * 0.350, canvas["w"] * 0.525],
                    "loc_y": [canvas["h"] * 0.625, canvas["h"] * 0.410, canvas["h"] * 0.625]
                }
            }
        }
    },  # DONE
    "per cross": {
        "dexter-chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.225],
                    "loc_y": [canvas["h"] * 0.05, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.04, canvas["w"] * 0.26, canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.225]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.225],
                    "loc_y": [canvas["h"] * 0.05, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.04, canvas["w"] * 0.26, canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.225]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.11, canvas["w"] * 0.25],
                    "loc_y": [canvas["h"] * 0.045, canvas["h"] * 0.2]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.11, canvas["w"] * 0.21, canvas["w"] * 0.31],
                    "loc_y": [canvas["h"] * 0.05, canvas["h"] * 0.2, canvas["h"] * 0.05]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.02, canvas["w"] * 0.18],
                    "loc_y": [canvas["h"] * 0.025, canvas["h"] * 0.25]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.04, canvas["w"] * 0.26, canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.085, canvas["h"] * 0.085, canvas["h"] * 0.265]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.225],
                    "loc_y": [canvas["h"] * 0.05, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.04, canvas["w"] * 0.26, canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.225]
                }
            }
        },
        "dexter-base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.225],
                    "loc_y": [canvas["h"] * 0.670, canvas["h"] * 0.493]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.055, canvas["w"] * 0.275],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.700, canvas["h"] * 0.600]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.150, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.670, canvas["h"] * 0.505]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.275, canvas["w"] * 0.055, canvas["w"] * 0.275],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.600, canvas["h"] * 0.700]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.275],
                    "loc_y": [canvas["h"] * 0.4]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.295, canvas["w"] * 0.320],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.285, canvas["w"] * 0.310, canvas["w"] * 0.335],
                    "loc_y": [canvas["h"] * 0.390, canvas["h"] * 0.495, canvas["h"] * 0.600]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.6]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.020, canvas["w"] * 0.180],
                    "loc_y": [canvas["h"] * 0.750, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.040, canvas["w"] * 0.260, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.765, canvas["h"] * 0.765, canvas["h"] * 0.585]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.150, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.670, canvas["h"] * 0.505]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.275, canvas["w"] * 0.055, canvas["w"] * 0.275],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.600, canvas["h"] * 0.700]
                }
            }
        },
        "sinister-chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.760, canvas["w"] * 0.540, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.225]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.760, canvas["w"] * 0.540, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.225]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.690, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.045, canvas["h"] * 0.200]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.740, canvas["w"] * 0.640, canvas["w"] * 0.540],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.200, canvas["h"] * 0.050]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.680, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.025, canvas["h"] * 0.250]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.760, canvas["w"] * 0.540, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.085, canvas["h"] * 0.085, canvas["h"] * 0.265]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.760, canvas["w"] * 0.540, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.225]
                }
            }
        },
        "sinister-base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.670, canvas["h"] * 0.493]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.755, canvas["w"] * 0.535, canvas["w"] * 0.755],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.600, canvas["h"] * 0.700]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.670, canvas["h"] * 0.505]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.525, canvas["w"] * 0.525, canvas["w"] * 0.745],
                    "loc_y": [canvas["h"] * 0.700, canvas["h"] * 0.500, canvas["h"] * 0.600]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.525],
                    "loc_y": [canvas["h"] * 0.4]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.555, canvas["w"] * 0.530],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.565, canvas["w"] * 0.540, canvas["w"] * 0.515],
                    "loc_y": [canvas["h"] * 0.390, canvas["h"] * 0.495, canvas["h"] * 0.600]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.6]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.680, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.750, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.760, canvas["w"] * 0.540, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.765, canvas["h"] * 0.765, canvas["h"] * 0.585]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.670, canvas["h"] * 0.505]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.525, canvas["w"] * 0.525, canvas["w"] * 0.745],
                    "loc_y": [canvas["h"] * 0.700, canvas["h"] * 0.500, canvas["h"] * 0.600]
                }
            }
        }
    },  # DONE
    "per fess": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100, canvas["h"] * 0.100]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100, canvas["h"] * 0.100]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.180, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.080, canvas["h"] * 0.080]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.150, canvas["w"] * 0.400, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.080, canvas["h"] * 0.140, canvas["h"] * 0.080]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.125, canvas["h"] * 0.125]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100, canvas["h"] * 0.100]
                }
            }
        },
        "base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.490, canvas["h"] * 0.490]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.600, canvas["h"] * 0.490, canvas["h"] * 0.600]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.55]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.500]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.350, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.480, canvas["h"] * 0.700, canvas["h"] * 0.480]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.290, canvas["w"] * 0.400, canvas["w"] * 0.510],
                    "loc_y": [canvas["h"] * 0.410, canvas["h"] * 0.600, canvas["h"] * 0.410]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.6]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.600, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.350, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.625, canvas["h"] * 0.625, canvas["h"] * 0.625]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.080, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.500]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.350, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.480, canvas["h"] * 0.690, canvas["h"] * 0.480]
                }
            }
        }
    },  # DONE
    "per pale": {
        "dexter": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.450]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.100, canvas["w"] * 0.100],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.300, canvas["h"] * 0.550]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.450]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.100, canvas["w"] * 0.100],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.300, canvas["h"] * 0.550]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.175],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.180, canvas["w"] * 0.255],
                    "loc_y": [canvas["h"] * 0.080, canvas["h"] * 0.255]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.105, canvas["w"] * 0.195, canvas["w"] * 0.285],
                    "loc_y": [canvas["h"] * 0.070, canvas["h"] * 0.200, canvas["h"] * 0.070]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.35]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.550]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.100, canvas["w"] * 0.100],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.400, canvas["h"] * 0.675]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.450]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.100, canvas["w"] * 0.100],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.300, canvas["h"] * 0.550]
                }
            }
        },
        "sinister": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.450]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.600, canvas["w"] * 0.600, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.300, canvas["h"] * 0.550]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.450]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.600, canvas["w"] * 0.600, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.300, canvas["h"] * 0.550]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.525],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.620, canvas["w"] * 0.545],
                    "loc_y": [canvas["h"] * 0.080, canvas["h"] * 0.255]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.655, canvas["w"] * 0.565],
                    "loc_y": [canvas["h"] * 0.070, canvas["h"] * 0.200, canvas["h"] * 0.070]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.35]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.550]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.600, canvas["w"] * 0.600, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.400, canvas["h"] * 0.675]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.450]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.600, canvas["w"] * 0.600, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.300, canvas["h"] * 0.550]
                }
            }
        }
    },  # DONE
    "per pall": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225, canvas["h"] * 0.050]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225, canvas["h"] * 0.050]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.060]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.030, canvas["h"] * 0.030]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.290, canvas["w"] * 0.425, canvas["w"] * 0.560],
                    "loc_y": [canvas["h"] * 0.030, canvas["h"] * 0.150, canvas["h"] * 0.030]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225, canvas["h"] * 0.050]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225, canvas["h"] * 0.050]
                }
            }
        },
        "dexter": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.065, canvas["w"] * 0.065],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.055, canvas["w"] * 0.205],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.700, canvas["h"] * 0.500]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.625]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.205, canvas["w"] * 0.130],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.700, canvas["h"] * 0.500]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.275],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.315],
                    "loc_y": [canvas["h"] * 0.275, canvas["h"] * 0.425]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.175, canvas["w"] * 0.325, canvas["w"] * 0.250],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.500, canvas["h"] * 0.350]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.55]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.700]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.055, canvas["w"] * 0.200],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.800, canvas["h"] * 0.550]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.625]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.055, canvas["w"] * 0.205, canvas["w"] * 0.130],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.700, canvas["h"] * 0.500]
                }
            }
        },
        "sinister": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.635, canvas["w"] * 0.635],
                    "loc_y": [canvas["h"] * 0.350, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.745, canvas["w"] * 0.595],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.700, canvas["h"] * 0.500]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.625]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.595, canvas["w"] * 0.670],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.700, canvas["h"] * 0.500]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.525],
                    "loc_y": [canvas["h"] * 0.300]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.600, canvas["w"] * 0.535],
                    "loc_y": [canvas["h"] * 0.275, canvas["h"] * 0.425]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.675, canvas["w"] * 0.525, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.500, canvas["h"] * 0.350]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.550]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.700]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.745, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.800, canvas["h"] * 0.550]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.475]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.625]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.745, canvas["w"] * 0.595, canvas["w"] * 0.670],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.700, canvas["h"] * 0.500]
                }
            }
        }
    },  # DONE
    "per saltire": {
        "base": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.560]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.330, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.600, canvas["h"] * 0.600]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.190, canvas["w"] * 0.425, canvas["w"] * 0.660],
                    "loc_y": [canvas["h"] * 0.715, canvas["h"] * 0.550, canvas["h"] * 0.715]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.610]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.700, canvas["h"] * 0.700]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.750, canvas["h"] * 0.550, canvas["h"] * 0.750]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.445, canvas["h"] * 0.615]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.335, canvas["w"] * 0.425, canvas["w"] * 0.515],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.630, canvas["h"] * 0.500]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.700]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.750, canvas["h"] * 0.750]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.815, canvas["h"] * 0.615, canvas["h"] * 0.815]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.605]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.690, canvas["h"] * 0.690]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.725, canvas["h"] * 0.550, canvas["h"] * 0.725]
                }
            }
        },
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.060]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.060, canvas["h"] * 0.060]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.025, canvas["h"] * 0.200, canvas["h"] * 0.025]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.060]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.060, canvas["h"] * 0.060]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.025, canvas["h"] * 0.200, canvas["h"] * 0.025]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.060]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.030, canvas["h"] * 0.030]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.290, canvas["w"] * 0.425, canvas["w"] * 0.560],
                    "loc_y": [canvas["h"] * 0.040, canvas["h"] * 0.160, canvas["h"] * 0.040]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.225, canvas["h"] * 0.050]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.060]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.060, canvas["h"] * 0.060]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.250, canvas["w"] * 0.400, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.025, canvas["h"] * 0.200, canvas["h"] * 0.025]
                }
            }
        },
        "dexter": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.290, canvas["h"] * 0.460]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.150, canvas["w"] * 0.025],
                    "loc_y": [canvas["h"] * 0.183, canvas["h"] * 0.353, canvas["h"] * 0.523]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.290, canvas["h"] * 0.460]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.150, canvas["w"] * 0.025],
                    "loc_y": [canvas["h"] * 0.183, canvas["h"] * 0.353, canvas["h"] * 0.523]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.230],
                    "loc_y": [canvas["h"] * 0.300]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.180, canvas["w"] * 0.230],
                    "loc_y": [canvas["h"] * 0.235, canvas["h"] * 0.345]
                },
                3: {
                    "size": charge_size["xs"],  # yeah i know it aint pretty :/
                    "loc_x": [canvas["w"] * 0.125, canvas["w"] * 0.195, canvas["w"] * 0.265],
                    "loc_y": [canvas["h"] * 0.150, canvas["h"] * 0.250, canvas["h"] * 0.350]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.378]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.550]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.150, canvas["w"] * 0.025],
                    "loc_y": [canvas["h"] * 0.228, canvas["h"] * 0.428, canvas["h"] * 0.628]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.290, canvas["h"] * 0.460]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.150, canvas["w"] * 0.025],
                    "loc_y": [canvas["h"] * 0.183, canvas["h"] * 0.353, canvas["h"] * 0.523]
                }
            }
        },
        "sinister": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.290, canvas["h"] * 0.460]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.775, canvas["w"] * 0.650, canvas["w"] * 0.775],
                    "loc_y": [canvas["h"] * 0.183, canvas["h"] * 0.353, canvas["h"] * 0.523]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.290, canvas["h"] * 0.460]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.775, canvas["w"] * 0.650, canvas["w"] * 0.775],
                    "loc_y": [canvas["h"] * 0.183, canvas["h"] * 0.353, canvas["h"] * 0.523]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.620],
                    "loc_y": [canvas["h"] * 0.300]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.670, canvas["w"] * 0.620],
                    "loc_y": [canvas["h"] * 0.235, canvas["h"] * 0.345]
                },
                3: {
                    "size": charge_size["xs"],  # yeah i know it aint pretty :/
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.655, canvas["w"] * 0.585],
                    "loc_y": [canvas["h"] * 0.150, canvas["h"] * 0.250, canvas["h"] * 0.350]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.378]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.550]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.775, canvas["w"] * 0.650, canvas["w"] * 0.775],
                    "loc_y": [canvas["h"] * 0.228, canvas["h"] * 0.428, canvas["h"] * 0.628]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.290, canvas["h"] * 0.460]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.775, canvas["w"] * 0.650, canvas["w"] * 0.775],
                    "loc_y": [canvas["h"] * 0.183, canvas["h"] * 0.353, canvas["h"] * 0.523]
                }
            }
        }
    },  # DONE
}

needs_flip = {
    "anchor": False,
    "bee": False,
    "castle": False,
    "dolphin": True,
    "eagle": True,
    "sun": False,
}
