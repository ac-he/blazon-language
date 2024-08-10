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
                    "size": charge_size["l"],
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
                    "loc_x": [canvas["w"] * 0.1],
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
                    "loc_x": [canvas["w"] * 0.15],
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
                    "loc_x": [canvas["w"] * 0.1],
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
                    "loc_x": [canvas["w"] * 0.45],
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
                    "loc_x": [canvas["w"] * 0.5],
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
                    "loc_x": [canvas["w"] * 0.45],
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
                    "loc_x": [canvas["w"] * 0.45],
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
                    "loc_y": [canvas["h"] * 0.075]
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
                    "loc_x": [canvas["w"] * 0.15],
                    "loc_y": [canvas["h"] * 0.075]
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
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.075]
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
        "dexter-base": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
                    "loc_y": [canvas["h"] * 0.475]
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
                    "loc_y": [canvas["h"] * 0.475]
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
                    "loc_x": [canvas["w"] * 0.05],
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
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.05],
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
        },
        "sinister-chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.075]
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
                    "loc_y": [canvas["h"] * 0.075]
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
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.075]
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
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
                    "loc_y": [canvas["h"] * 0.075]
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
                    "loc_y": [canvas["h"] * 0.475]
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
                    "loc_y": [canvas["h"] * 0.475]
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
                    "loc_x": [canvas["w"] * 0.55],
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
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.55],
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
    "per fess": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.075]
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
                    "loc_y": [canvas["h"] * 0.075]
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
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.3],
                    "loc_y": [canvas["h"] * 0.075]
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
