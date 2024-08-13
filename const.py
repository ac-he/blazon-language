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
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.05, canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.35, canvas["h"] * 0.6]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.1],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.65]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.4]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.225, canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.275, canvas["h"] * 0.5]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.55]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.675]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
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
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
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
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.375]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.45],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.375]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.6],
                    "loc_y": [canvas["h"] * 0.025, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.45],
                    "loc_y": [canvas["h"] * 0.15]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.375]
                },
                3: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.45],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.375]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        }
    },
    "per bend sinister": {
        "dexter-chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.2],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.15]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        },
        "sinister-base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.4]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.45],
                    "loc_y": [canvas["h"] * 0.55]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        }
    },
    "per chevron": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
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
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        },
        "base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.425]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
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
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.55]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        }
    },
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
    },
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
    },
    "per pale": {
        "dexter": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.175],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.35]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
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
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.525],
                    "loc_y": [canvas["h"] * 0.1]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.35]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        }
    },
    "per pall": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.025]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.025]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.025]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.025]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.025]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        },
        "dexter": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.275],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
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
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        },
        "sinister": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.525],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.55]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.45]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        }
    },
    "per saltire": {
        "base": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.55]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.6]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.5]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.675]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.6]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        },
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.025]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.05]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        },
        "dexter": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.35]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.225],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.375]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        },
        "sinister": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.65],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.65],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.575],
                    "loc_y": [canvas["h"] * 0.3]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.65],
                    "loc_y": [canvas["h"] * 0.375]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.65],
                    "loc_y": [canvas["h"] * 0.325]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.3, canvas["w"] * 0.4, canvas["w"] * 0.5],
                    "loc_y": [canvas["h"] * 0.1, canvas["h"] * 0.1, canvas["h"] * 0.1]
                }
            }
        }
    },
}

needs_flip = {
    "anchor": False,
    "bee": False,
    "castle": False,
    "dolphin": True,
    "eagle": True,
    "sun": False,
}
