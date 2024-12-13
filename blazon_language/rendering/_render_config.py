tinctures = {
    "argent": {"r": 243/255, "g": 243/255, "b": 243/255, "initial": "r", "type": "metal"},
    "or": {"r": 241/255, "g": 194/255, "b": 50/255, "initial": "o", "type": "metal"},
    "gules": {"r": 190/255, "g": 37/255, "b": 37/255, "initial": "g", "type": "color"},
    "vert": {"r": 78/255, "g": 111/255, "b": 52/255, "initial": "v", "type": "color"},
    "azure": {"r": 17/255, "g": 85/255, "b": 204/255, "initial": "a", "type": "color"},
    "sable": {"r": 22/255, "g": 22/255, "b": 22/255, "initial": "s", "type": "color"},
    "purpure": {"r": 130/255, "g": 77/255, "b": 121/255, "initial": "p", "type": "color"},
}

canvas = {
    "w": 600,
    "h": 800
}

shapes = ["banner", "heater", "pennant", "rect", "shield"]
divisions = ["per bend", "per bend sinister", "per chevron", "per cross", "per fess", "escutcheon",
             "per pale", "per pall", "per saltire", "none"]

colors = ["g", "s", "v", "a", "p"]
metals = ["o", "r"]
all_tinctures = ["g", "s", "v", "a", "p", "o", "r"]

shape_points = {
    "banner": [
        ["m", 0.000, 0.000],
        ["l", 0.000, 1.000],
        ["l", 0.500, 0.750],
        ["l", 1.000, 1.000],
        ["l", 1.000, 0.000]
    ],
    "heater": [
        ["m", 0.000, 0.000],
        ["l", 0.000, 0.625],
        [
            "c",
            [0.000, 0.875],
            [0.333, 0.936],
            [0.500, 1.000]
        ],
        [
            "c",
            [0.666, 0.936],
            [1.000, 0.875],
            [1.000, 0.625],
        ],
        ["l", 1.000, 0.000],
    ],
    "pennant": [
        ["m", 0.000, 0.000],
        ["l", 0.500, 1.000],
        ["l", 1.000, 0.000]
    ],
    "rect": [
        ["m", 0.000, 0.000],
        ["l", 1.000, 0.000],
        ["l", 1.000, 1.000],
        ["l", 0.000, 1.000]
    ],
    "shield": [
        ["m", 0.000, 0.000],
        ["l", 0.000, 0.750],
        [
            "c",
            [0.000, 0.875],
            [0.500, 0.875],
            [0.500, 1.000]
        ],
        [
            "c",
            [0.500, 0.875],
            [1.000, 0.875],
            [1.000, 0.750],
        ],
        ["l", 1.000, 0.000],
    ]
}

charge_size = {
    "f": 512,  # full
    "l": canvas["w"] * 0.4,  # large
    "m": canvas["w"] * 0.3,  # medium
    "s": canvas["w"] * 0.2,   # small
    "xs": canvas["w"] * 0.15     # x small
}

charge_detail = {
    "label": {
        "bend": {
            "field": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.610,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.120
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.610,
                    "center": canvas['w'] * 0.350,
                    "spacing": canvas['w'] * 0.150
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.590,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.100
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.610,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.120
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.610,
                    "center": canvas['w'] * 0.350,
                    "spacing": canvas['w'] * 0.120
                }
            },
        },
        "bend sinister": {
            "field": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.610,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.120
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.610,
                    "center": canvas['w'] * 0.650,
                    "spacing": canvas['w'] * 0.150
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.590,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.100
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.610,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.120
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.610,
                    "center": canvas['w'] * 0.650,
                    "spacing": canvas['w'] * 0.120
                }
            },
        },
        "chevron": {
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.040,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.075,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.060,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.075,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.040,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            },
            "ordinary": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.280,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.330,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.280,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.330,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.280,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                }
            },
            "base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.580,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.130
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.650,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            }
        },
        "escutcheon": {
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.070,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.300
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.070,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.300
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.070,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.250
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.070,
                    "bar_y": canvas['h'] * 0.070,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.300
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.070,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.300
                }
            },
            "base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.650,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.300
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.100
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.775,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            },
            "escutcheon": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.225,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.225,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.240,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.100
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.300,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.225,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                }
            },
        },
        "fess": {
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.075,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.075,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.060,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.075,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.075,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            },
            "ordinary": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.375,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.375,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.310,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.400,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.375,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            },
            "base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.620,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.650,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.130
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.715,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.675,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            }
        },
        "pale": {
            "dexter": {
                "banner": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.167,
                    "spacing": canvas['w'] * 0.085
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.167,
                    "spacing": canvas['w'] * 0.085
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.085
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.167,
                    "spacing": canvas['w'] * 0.085
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.167,
                    "spacing": canvas['w'] * 0.085
                }
            },
            "ordinary": {
                "banner": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.085
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.085
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.030,
                    "bar_y": canvas['h'] * 0.160,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.065
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.085
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.085
                }
            },
            "sinister": {
                "banner": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.833,
                    "spacing": canvas['w'] * 0.085
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.833,
                    "spacing": canvas['w'] * 0.085
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.085
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.833,
                    "spacing": canvas['w'] * 0.085
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.833,
                    "spacing": canvas['w'] * 0.085
                }
            }
        },
        "saltire": {
            "field": {
                "banner": {
                    "bar_h": canvas['h'] * 0.067,
                    "bar_y": canvas['h'] * 0.050,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.115
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.067,
                    "bar_y": canvas['h'] * 0.050,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.115
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.067,
                    "bar_y": canvas['h'] * 0.050,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.115
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.067,
                    "bar_y": canvas['h'] * 0.050,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.115
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.067,
                    "bar_y": canvas['h'] * 0.050,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.115
                }
            },
        },
        "per bend": {
            "base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.300,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.300,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.500,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.300,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.300,
                    "spacing": canvas['w'] * 0.200
                }
            },
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.625,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.625,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.160,
                    "center": canvas['w'] * 0.625,
                    "spacing": canvas['w'] * 0.150
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.625,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.625,
                    "spacing": canvas['w'] * 0.200
                }
            }
        },
        "per bend sinister": {
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.375,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.375,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.160,
                    "center": canvas['w'] * 0.375,
                    "spacing": canvas['w'] * 0.150
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.375,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.375,
                    "spacing": canvas['w'] * 0.200
                }
            },
            "base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.700,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.700,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.500,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.700,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.700,
                    "spacing": canvas['w'] * 0.200
                }
            },
        },
        "per chevron": {
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            },
            "base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.600,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.130
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.650,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            }
        },
        "per cross": {
            "dexter-chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.300,
                    "spacing": canvas['w'] * 0.135
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                }
            },
            "dexter-base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.030,
                    "bar_y": canvas['h'] * 0.450,
                    "center": canvas['w'] * 0.380,
                    "spacing": canvas['w'] * 0.085
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.650,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                }
            },
            "sinister-chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.700,
                    "spacing": canvas['w'] * 0.135
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                }
            },
            "sinister-base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.030,
                    "bar_y": canvas['h'] * 0.450,
                    "center": canvas['w'] * 0.620,
                    "spacing": canvas['w'] * 0.085
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.650,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                }
            }
        },
        "per fess": {
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            },
            "base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.430,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.150
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.650,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.200
                }
            }
        },
        "per pale": {
            "dexter": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.300,
                    "spacing": canvas['w'] * 0.135
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                }
            },
            "sinister": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.700,
                    "spacing": canvas['w'] * 0.135
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.150,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                }
            }
        },
        "per pall": {
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.180
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.180
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.050,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.130
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.180
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.180
                }
            },
            "dexter": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.035,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.345,
                    "spacing": canvas['w'] * 0.095
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.250,
                    "spacing": canvas['w'] * 0.155
                }
            },
            "sinister": {
                "banner": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.035,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.655,
                    "spacing": canvas['w'] * 0.095
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.065,
                    "bar_y": canvas['h'] * 0.550,
                    "center": canvas['w'] * 0.750,
                    "spacing": canvas['w'] * 0.155
                }
            }
        },
        "per saltire": {
            "base": {
                "banner": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.600,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.155
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.180
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.045,
                    "bar_y": canvas['h'] * 0.575,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.125
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.180
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.700,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.180
                }
            },
            "chief": {
                "banner": {
                    "bar_h": canvas['h'] * 0.070,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.160
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.070,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.160
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.090,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.140
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.075,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.180
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.070,
                    "bar_y": canvas['h'] * 0.100,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.160
                }
            },
            "dexter": {
                "banner": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.230,
                    "spacing": canvas['w'] * 0.140
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.230,
                    "spacing": canvas['w'] * 0.140
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.035,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.335,
                    "spacing": canvas['w'] * 0.070
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.230,
                    "spacing": canvas['w'] * 0.140
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.230,
                    "spacing": canvas['w'] * 0.140
                }
            },
            "sinister": {
                "banner": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.770,
                    "spacing": canvas['w'] * 0.140
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.770,
                    "spacing": canvas['w'] * 0.140
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.035,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.665,
                    "spacing": canvas['w'] * 0.070
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.770,
                    "spacing": canvas['w'] * 0.140
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.060,
                    "bar_y": canvas['h'] * 0.350,
                    "center": canvas['w'] * 0.770,
                    "spacing": canvas['w'] * 0.140
                }
            }
        },
        "per nothing": {
            "field": {
                "banner": {
                    "bar_h": canvas['h'] * 0.100,
                    "bar_y": canvas['h'] * 0.200,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.250
                },
                "heater": {
                    "bar_h": canvas['h'] * 0.100,
                    "bar_y": canvas['h'] * 0.200,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.250
                },
                "pennant": {
                    "bar_h": canvas['h'] * 0.080,
                    "bar_y": canvas['h'] * 0.200,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.210
                },
                "rect": {
                    "bar_h": canvas['h'] * 0.100,
                    "bar_y": canvas['h'] * 0.200,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.250
                },
                "shield": {
                    "bar_h": canvas['h'] * 0.100,
                    "bar_y": canvas['h'] * 0.200,
                    "center": canvas['w'] * 0.500,
                    "spacing": canvas['w'] * 0.250
                }
            },
        },
    },
    "qoe": {
        "bend": {
            "field": {
                "banner": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.400,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.600
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
        },
        "bend sinister": {
            "field": {
                "banner": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.400,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.600
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
        },
        "chevron": {
            "chief": {
                "banner": {
                    "fess": canvas['h'] * 0.150,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "rect": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.150,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
            "ordinary": {
                "banner": {
                    "fess": canvas['h'] * 0.415,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.480,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.375,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "rect": {
                    "fess": canvas['h'] * 0.480,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.415,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
            "base": {
                "banner": {
                    "fess": canvas['h'] * 0.675,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.735,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.400,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.600
                },
                "rect": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.700,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            }
        },
        "escutcheon": {
            "chief": {
                "banner": {
                    "fess": canvas['h'] * 0.100,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.100,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.100,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "rect": {
                    "fess": canvas['h'] * 0.100,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.100,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
            "base": {
                "banner": {
                    "fess": canvas['h'] * 0.725,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.400,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.600
                },
                "rect": {
                    "fess": canvas['h'] * 0.800,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
            "escutcheon": {
                "banner": {
                    "fess": canvas['h'] * 0.425,
                    "dexter": canvas['w'] * 0.375,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.625
                },
                "heater": {
                    "fess": canvas['h'] * 0.425,
                    "dexter": canvas['w'] * 0.375,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.625
                },
                "pennant": {
                    "fess": canvas['h'] * 0.350,
                    "dexter": canvas['w'] * 0.400,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.600
                },
                "rect": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.375,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.625
                },
                "shield": {
                    "fess": canvas['h'] * 0.425,
                    "dexter": canvas['w'] * 0.375,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.625
                }
            },
        },
        "fess": {
            "chief": {
                "banner": {
                    "fess": canvas['h'] * 0.140,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.140,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.130,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "rect": {
                    "fess": canvas['h'] * 0.170,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.140,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
            "ordinary": {
                "banner": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.375,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
            "base": {
                "banner": {
                    "fess": canvas['h'] * 0.700,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.400,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.600
                },
                "rect": {
                    "fess": canvas['h'] * 0.825,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            }
        },
        "pale": {
            "dexter": {
                "banner": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.167,
                },
                "heater": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.167,
                },
                "pennant": {
                    "chief": canvas['h'] * 0.120,
                    "fess": canvas['h'] * 0.240,
                    "base": canvas['h'] * 0.360,
                    "pale": canvas['w'] * 0.275,
                },
                "rect": {
                    "chief": canvas['h'] * 0.250,
                    "fess": canvas['h'] * 0.500,
                    "base": canvas['h'] * 0.750,
                    "pale": canvas['w'] * 0.167,
                },
                "shield": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.167,
                }
            },
            "ordinary": {
                "banner": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.500,
                },
                "heater": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.500,
                },
                "pennant": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.500,
                },
                "rect": {
                    "chief": canvas['h'] * 0.250,
                    "fess": canvas['h'] * 0.500,
                    "base": canvas['h'] * 0.750,
                    "pale": canvas['w'] * 0.500,
                },
                "shield": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.500,
                }
            },
            "sinister": {
                "banner": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.833,
                },
                "heater": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.833,
                },
                "pennant": {
                    "chief": canvas['h'] * 0.120,
                    "fess": canvas['h'] * 0.240,
                    "base": canvas['h'] * 0.360,
                    "pale": canvas['w'] * 0.725,
                },
                "rect": {
                    "chief": canvas['h'] * 0.250,
                    "fess": canvas['h'] * 0.500,
                    "base": canvas['h'] * 0.750,
                    "pale": canvas['w'] * 0.833,
                },
                "shield": {
                    "chief": canvas['h'] * 0.200,
                    "fess": canvas['h'] * 0.450,
                    "base": canvas['h'] * 0.700,
                    "pale": canvas['w'] * 0.833,
                }
            }
        },
        "saltire": {
            "field": {
                "banner": {
                    "fess": canvas['h'] * 0.438,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.438,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.375,
                    "dexter": canvas['w'] * 0.300,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.700
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.438,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
        },
        "per bend": {
            "dexter-base": {
                "banner": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.167,
                    "pale": canvas['w'] * 0.333,
                    "sinister": canvas['w'] * 0.500
                },
                "heater": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.167,
                    "pale": canvas['w'] * 0.333,
                    "sinister": canvas['w'] * 0.500
                },
                "pennant": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.400,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.600
                },
                "rect": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.167,
                    "pale": canvas['w'] * 0.333,
                    "sinister": canvas['w'] * 0.500
                },
                "shield": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.167,
                    "pale": canvas['w'] * 0.333,
                    "sinister": canvas['w'] * 0.500
                }
            },
            "sinister-chief": {
                "banner": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.500,
                    "pale": canvas['w'] * 0.667,
                    "sinister": canvas['w'] * 0.833
                },
                "heater": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.500,
                    "pale": canvas['w'] * 0.667,
                    "sinister": canvas['w'] * 0.833
                },
                "pennant": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.450,
                    "pale": canvas['w'] * 0.600,
                    "sinister": canvas['w'] * 0.750
                },
                "rect": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.500,
                    "pale": canvas['w'] * 0.667,
                    "sinister": canvas['w'] * 0.833
                },
                "shield": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.500,
                    "pale": canvas['w'] * 0.667,
                    "sinister": canvas['w'] * 0.833
                }
            }
        },
        "per bend sinister": {
            "dexter-chief": {
                "banner": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.167,
                    "pale": canvas['w'] * 0.333,
                    "sinister": canvas['w'] * 0.500
                },
                "heater": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.167,
                    "pale": canvas['w'] * 0.333,
                    "sinister": canvas['w'] * 0.500
                },
                "pennant": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.400,
                    "sinister": canvas['w'] * 0.550
                },
                "rect": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.167,
                    "pale": canvas['w'] * 0.333,
                    "sinister": canvas['w'] * 0.500
                },
                "shield": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.167,
                    "pale": canvas['w'] * 0.333,
                    "sinister": canvas['w'] * 0.500
                }
            },
            "sinister-base": {
                "banner": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.500,
                    "pale": canvas['w'] * 0.667,
                    "sinister": canvas['w'] * 0.833
                },
                "heater": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.500,
                    "pale": canvas['w'] * 0.667,
                    "sinister": canvas['w'] * 0.833
                },
                "pennant": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.400,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.600
                },
                "rect": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.500,
                    "pale": canvas['w'] * 0.667,
                    "sinister": canvas['w'] * 0.833
                },
                "shield": {
                    "fess": canvas['h'] * 0.600,
                    "dexter": canvas['w'] * 0.500,
                    "pale": canvas['w'] * 0.667,
                    "sinister": canvas['w'] * 0.833
                }
            },
        },
        "per chevron": {
            "chief": {
                "banner": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "rect": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
            "base": {
                "banner": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "rect": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            }
        },
        "per cross": {
            "dexter-chief": {
                "banner": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "heater": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "pennant": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.200,
                    "pale": canvas['w'] * 0.300,
                    "sinister": canvas['w'] * 0.400
                },
                "rect": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "shield": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                }
            },
            "dexter-base": {
                "banner": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "heater": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "pennant": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.400,
                    "sinister": canvas['w'] * 0.450
                },
                "rect": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "shield": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                }
            },
            "sinister-chief": {
                "banner": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "heater": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "pennant": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.600,
                    "pale": canvas['w'] * 0.700,
                    "sinister": canvas['w'] * 0.800
                },
                "rect": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "shield": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                }
            },
            "sinister-base": {
                "banner": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "heater": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "pennant": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.550,
                    "pale": canvas['w'] * 0.600,
                    "sinister": canvas['w'] * 0.650
                },
                "rect": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "shield": {
                    "fess": canvas['h'] * 0.650,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                }
            }
        },
        "per fess": {
            "chief": {
                "banner": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "rect": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.225,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
            "base": {
                "banner": {
                    "fess": canvas['h'] * 0.675,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.675,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "rect": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.675,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            }
        },
        "per pale": {
            "dexter": {
                "banner": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "heater": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "pennant": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.200,
                    "pale": canvas['w'] * 0.300,
                    "sinister": canvas['w'] * 0.400
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "shield": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                }
            },
            "sinister": {
                "banner": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "heater": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "pennant": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.600,
                    "pale": canvas['w'] * 0.700,
                    "sinister": canvas['w'] * 0.800
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "shield": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                }
            }
        },
        "per pall": {
            "chief": {
                "banner": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "heater": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "pennant": {
                    "fess": canvas['h'] * 0.125,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "rect": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "shield": {
                    "fess": canvas['h'] * 0.200,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                }
            },
            "dexter": {
                "banner": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "heater": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "pennant": {
                    "fess": canvas['h'] * 0.315,
                    "dexter": canvas['w'] * 0.200,
                    "pale": canvas['w'] * 0.300,
                    "sinister": canvas['w'] * 0.400
                },
                "rect": {
                    "fess": canvas['h'] * 0.625,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "shield": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                }
            },
            "sinister": {
                "banner": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "heater": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "pennant": {
                    "fess": canvas['h'] * 0.315,
                    "dexter": canvas['w'] * 0.600,
                    "pale": canvas['w'] * 0.700,
                    "sinister": canvas['w'] * 0.800
                },
                "rect": {
                    "fess": canvas['h'] * 0.625,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "shield": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                }
            }
        },
        "per saltire": {
            "base": {
                "banner": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.810,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.550,
                    "dexter": canvas['w'] * 0.375,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.625
                },
                "rect": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "shield": {
                    "fess": canvas['h'] * 0.750,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                }
            },
            "chief": {
                "banner": {
                    "fess": canvas['h'] * 0.150,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.150,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.150,
                    "dexter": canvas['w'] * 0.375,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.625
                },
                "rect": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                },
                "shield": {
                    "fess": canvas['h'] * 0.100,
                    "dexter": canvas['w'] * 0.350,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.650
                }
            },
            "dexter": {
                "banner": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "heater": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "pennant": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.200,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.300
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                },
                "shield": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.125,
                    "pale": canvas['w'] * 0.250,
                    "sinister": canvas['w'] * 0.375
                }
            },
            "sinister": {
                "banner": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "heater": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "pennant": {
                    "fess": canvas['h'] * 0.300,
                    "dexter": canvas['w'] * 0.700,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.800
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                },
                "shield": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.625,
                    "pale": canvas['w'] * 0.750,
                    "sinister": canvas['w'] * 0.875
                }
            }
        },
        "per nothing": {
            "field": {
                "banner": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "heater": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "pennant": {
                    "fess": canvas['h'] * 0.250,
                    "dexter": canvas['w'] * 0.300,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.700
                },
                "rect": {
                    "fess": canvas['h'] * 0.500,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                },
                "shield": {
                    "fess": canvas['h'] * 0.450,
                    "dexter": canvas['w'] * 0.250,
                    "pale": canvas['w'] * 0.500,
                    "sinister": canvas['w'] * 0.750
                }
            },
        },
    }
}

charge_loc = {
    "bend": {
        "field": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.065],
                    "loc_y": [canvas["h"] * 0.480]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.065, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.480, canvas["h"] * 0.040]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.310, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.560, canvas["h"] * 0.150]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.220],
                    "loc_y": [canvas["h"] * 0.600]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.065, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.480, canvas["h"] * 0.040]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.600, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.100, canvas["h"] * 0.675]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.470]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.470, canvas["h"] * 0.025]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.280, canvas["w"] * 0.400, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.610, canvas["h"] * 0.075]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.100],
                    "loc_y": [canvas["h"] * 0.650]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.510],
                    "loc_y": [canvas["h"] * 0.650, canvas["h"] * 0.050]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.600, canvas["w"] * 0.315],
                    "loc_y": [canvas["h"] * 0.525, canvas["h"] * 0.100, canvas["h"] * 0.750]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.100],
                    "loc_y": [canvas["h"] * 0.510]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.065, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.480, canvas["h"] * 0.040]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.600, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.100, canvas["h"] * 0.675]
                }
            }
        },
    },
    "bend sinister": {
        "field": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.535],
                    "loc_y": [canvas["h"] * 0.480]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.535, canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.480, canvas["h"] * 0.040]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.490, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.375, canvas["h"] * 0.560, canvas["h"] * 0.150]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.380],
                    "loc_y": [canvas["h"] * 0.600]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.535, canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.480, canvas["h"] * 0.040]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.625, canvas["w"] * 0.100, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.100, canvas["h"] * 0.675]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.470]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350, canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.470, canvas["h"] * 0.025]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.520, canvas["w"] * 0.400, canvas["w"] * 0.200],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.610, canvas["h"] * 0.075]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.500],
                    "loc_y": [canvas["h"] * 0.650]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.500, canvas["w"] * 0.090],
                    "loc_y": [canvas["h"] * 0.650, canvas["h"] * 0.050]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.625, canvas["w"] * 0.100, canvas["w"] * 0.385],
                    "loc_y": [canvas["h"] * 0.525, canvas["h"] * 0.100, canvas["h"] * 0.750]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.500],
                    "loc_y": [canvas["h"] * 0.510]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.535, canvas["w"] * 0.050],
                    "loc_y": [canvas["h"] * 0.480, canvas["h"] * 0.040]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.625, canvas["w"] * 0.100, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.100, canvas["h"] * 0.675]
                }
            }
        },
    },
    "chevron": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.023]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.143, canvas["h"] * 0.023, canvas["h"] * 0.143]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.085, canvas["w"] * 0.615],
                    "loc_y": [canvas["h"] * 0.085, canvas["h"] * 0.085]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.160, canvas["h"] * 0.040, canvas["h"] * 0.160]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.023]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.150, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.140, canvas["w"] * 0.400, canvas["w"] * 0.660],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.023, canvas["h"] * 0.100]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.085, canvas["w"] * 0.615],
                    "loc_y": [canvas["h"] * 0.085, canvas["h"] * 0.085]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.160, canvas["h"] * 0.040, canvas["h"] * 0.160]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.023]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.143, canvas["h"] * 0.023, canvas["h"] * 0.143]
                }
            }
        },
        "ordinary": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.250]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.380, canvas["h"] * 0.380]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.380, canvas["h"] * 0.255, canvas["h"] * 0.380]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.300]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.435, canvas["h"] * 0.435]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.445, canvas["h"] * 0.300, canvas["h"] * 0.445]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.250]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.300, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.320, canvas["h"] * 0.320]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.270, canvas["w"] * 0.425, canvas["w"] * 0.580],
                    "loc_y": [canvas["h"] * 0.340, canvas["h"] * 0.270, canvas["h"] * 0.340]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.300]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.435, canvas["h"] * 0.435]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.445, canvas["h"] * 0.310, canvas["h"] * 0.445]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.250]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.380, canvas["h"] * 0.380]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.380, canvas["h"] * 0.255, canvas["h"] * 0.380]
                }
            }
        },
        "base": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.500]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.660, canvas["h"] * 0.660]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.660, canvas["h"] * 0.530, canvas["h"] * 0.660]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.590]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.160, canvas["w"] * 0.540],
                    "loc_y": [canvas["h"] * 0.650, canvas["h"] * 0.650]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.240, canvas["w"] * 0.400, canvas["w"] * 0.560],
                    "loc_y": [canvas["h"] * 0.750, canvas["h"] * 0.550, canvas["h"] * 0.750]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.35],
                    "loc_y": [canvas["h"] * 0.500]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.425, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.485, canvas["h"] * 0.650]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.320, canvas["w"] * 0.425, canvas["w"] * 0.530],
                    "loc_y": [canvas["h"] * 0.520, canvas["h"] * 0.670, canvas["h"] * 0.520]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.620]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.130, canvas["w"] * 0.570],
                    "loc_y": [canvas["h"] * 0.700, canvas["h"] * 0.700]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.200, canvas["w"] * 0.400, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.780, canvas["h"] * 0.580, canvas["h"] * 0.780]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.570]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.130, canvas["w"] * 0.570],
                    "loc_y": [canvas["h"] * 0.620, canvas["h"] * 0.620]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.230, canvas["w"] * 0.400, canvas["w"] * 0.570],
                    "loc_y": [canvas["h"] * 0.695, canvas["h"] * 0.485, canvas["h"] * 0.695]
                }
            }
        }
    },
    "escutcheon": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.028]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.030, canvas["w"] * 0.770],
                    "loc_y": [canvas["h"] * 0.030, canvas["h"] * 0.030]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.030, canvas["w"] * 0.400, canvas["w"] * 0.770],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.028, canvas["h"] * 0.125]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.028]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.030, canvas["w"] * 0.770],
                    "loc_y": [canvas["h"] * 0.030, canvas["h"] * 0.030]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.030, canvas["w"] * 0.400, canvas["w"] * 0.770],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.028, canvas["h"] * 0.125]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.028]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.065, canvas["h"] * 0.065]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.065, canvas["h"] * 0.028, canvas["h"] * 0.065]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.020]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.020, canvas["h"] * 0.020]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.030, canvas["w"] * 0.400, canvas["w"] * 0.770],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.050, canvas["h"] * 0.125]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.028]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.030, canvas["w"] * 0.770],
                    "loc_y": [canvas["h"] * 0.030, canvas["h"] * 0.030]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.030, canvas["w"] * 0.400, canvas["w"] * 0.770],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.028, canvas["h"] * 0.125]
                }
            }
        },
        "base": {
            "banner": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025],
                    "loc_y": [canvas["h"] * 0.625]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.675],
                    "loc_y": [canvas["h"] * 0.625, canvas["h"] * 0.625]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.025, canvas["w"] * 0.025, canvas["w"] * 0.775],
                    "loc_y": [canvas["h"] * 0.700, canvas["h"] * 0.490, canvas["h"] * 0.595]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.720]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.110, canvas["w"] * 0.590],
                    "loc_y": [canvas["h"] * 0.635, canvas["h"] * 0.635]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.400, canvas["w"] * 0.750],
                    "loc_y": [canvas["h"] * 0.540, canvas["h"] * 0.745, canvas["h"] * 0.540]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.600]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.425, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.580, canvas["h"] * 0.700]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.335, canvas["w"] * 0.425, canvas["w"] * 0.515],
                    "loc_y": [canvas["h"] * 0.570, canvas["h"] * 0.700, canvas["h"] * 0.570]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.760]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.110, canvas["w"] * 0.590],
                    "loc_y": [canvas["h"] * 0.725, canvas["h"] * 0.725]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.400, canvas["w"] * 0.750],
                    "loc_y": [canvas["h"] * 0.580, canvas["h"] * 0.775, canvas["h"] * 0.580]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.695]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.620, canvas["h"] * 0.620]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.400, canvas["w"] * 0.750],
                    "loc_y": [canvas["h"] * 0.540, canvas["h"] * 0.745, canvas["h"] * 0.540]
                }
            }
        },
        "escutcheon": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.280]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.300, canvas["w"] * 0.500],
                    "loc_y": [canvas["h"] * 0.260, canvas["h"] * 0.420]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.460, canvas["h"] * 0.260, canvas["h"] * 0.260]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.280]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.300, canvas["w"] * 0.500],
                    "loc_y": [canvas["h"] * 0.260, canvas["h"] * 0.420]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.460, canvas["h"] * 0.260, canvas["h"] * 0.260]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.250]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.375, canvas["w"] * 0.470],
                    "loc_y": [canvas["h"] * 0.250, canvas["h"] * 0.375]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.340, canvas["w"] * 0.425, canvas["w"] * 0.510],
                    "loc_y": [canvas["h"] * 0.250, canvas["h"] * 0.375, canvas["h"] * 0.250]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.330]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.320, canvas["w"] * 0.480],
                    "loc_y": [canvas["h"] * 0.320, canvas["h"] * 0.480]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.500, canvas["h"] * 0.340, canvas["h"] * 0.340]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.280]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.300, canvas["w"] * 0.500],
                    "loc_y": [canvas["h"] * 0.260, canvas["h"] * 0.420]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.280, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.460, canvas["h"] * 0.260, canvas["h"] * 0.260]
                }
            }
        },
    },
    "fess": {
        "chief": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.200, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.200, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.050]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.150, canvas["w"] * 0.400, canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.050, canvas["h"] * 0.050]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.130, canvas["w"] * 0.570],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075],
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.100, canvas["h"] * 0.100]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.200, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.075, canvas["h"] * 0.075]
                }
            }
        },
        "ordinary": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.365]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.365, canvas["h"] * 0.365]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.365, canvas["h"] * 0.365, canvas["h"] * 0.365]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.365]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.200, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.365, canvas["h"] * 0.365]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.365, canvas["h"] * 0.365, canvas["h"] * 0.365]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.300]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.300, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.320, canvas["h"] * 0.320]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.270, canvas["w"] * 0.425, canvas["w"] * 0.580],
                    "loc_y": [canvas["h"] * 0.285, canvas["h"] * 0.355, canvas["h"] * 0.285]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.400]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.130, canvas["w"] * 0.570],
                    "loc_y": [canvas["h"] * 0.400, canvas["h"] * 0.400],
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.425, canvas["h"] * 0.425]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.365]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.200, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.365, canvas["h"] * 0.380]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.365, canvas["h"] * 0.365, canvas["h"] * 0.365]
                }
            }
        },
        "base": {
            "banner": {
                1: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.610]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.660, canvas["h"] * 0.660]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.120, canvas["w"] * 0.425, canvas["w"] * 0.730],
                    "loc_y": [canvas["h"] * 0.700, canvas["h"] * 0.610, canvas["h"] * 0.700]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.620]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.200, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.670, canvas["h"] * 0.670]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.140, canvas["w"] * 0.400, canvas["w"] * 0.660],
                    "loc_y": [canvas["h"] * 0.670, canvas["h"] * 0.720, canvas["h"] * 0.670]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.575]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.425, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.525, canvas["h"] * 0.675]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.335, canvas["w"] * 0.425, canvas["w"] * 0.515],
                    "loc_y": [canvas["h"] * 0.520, canvas["h"] * 0.650, canvas["h"] * 0.520]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.710]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.130, canvas["w"] * 0.570],
                    "loc_y": [canvas["h"] * 0.710, canvas["h"] * 0.710]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.750, canvas["h"] * 0.750, canvas["h"] * 0.750]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.650]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.200, canvas["w"] * 0.600],
                    "loc_y": [canvas["h"] * 0.650, canvas["h"] * 0.650]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.400, canvas["w"] * 0.700],
                    "loc_y": [canvas["h"] * 0.650, canvas["h"] * 0.690, canvas["h"] * 0.650]
                }
            }
        }
    },
    "pale": {
        "dexter": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.400]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.275, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.150, canvas["h"] * 0.400, canvas["h"] * 0.650]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.350]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.225, canvas["h"] * 0.475]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.350, canvas["h"] * 0.600]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.150],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.150, canvas["w"] * 0.205],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.200]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.125, canvas["w"] * 0.180, canvas["w"] * 0.235],
                    "loc_y": [canvas["h"] * 0.025, canvas["h"] * 0.165, canvas["h"] * 0.305]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.425]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.550]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.175, canvas["h"] * 0.425, canvas["h"] * 0.675]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.350]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.225, canvas["h"] * 0.475]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.075, canvas["w"] * 0.075, canvas["w"] * 0.075],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.350, canvas["h"] * 0.600]
                }
            }
        },
        "ordinary": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.400]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.275, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.075, canvas["h"] * 0.300, canvas["h"] * 0.525]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.350]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.225, canvas["h"] * 0.475]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.225, canvas["h"] * 0.475, canvas["h"] * 0.725]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.300]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.425, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.400]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.425, canvas["w"] * 0.425, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.300, canvas["h"] * 0.500]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.425]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.550]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.175, canvas["h"] * 0.425, canvas["h"] * 0.675]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.350]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.225, canvas["h"] * 0.475]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.225, canvas["h"] * 0.475, canvas["h"] * 0.725]
                }
            }
        },
        "sinister": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.400]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.275, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.150, canvas["h"] * 0.400, canvas["h"] * 0.650]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.350]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.225, canvas["h"] * 0.475]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.350, canvas["h"] * 0.600]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.650],
                    "loc_y": [canvas["h"] * 0.075]
                },
                2: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.700, canvas["w"] * 0.645],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.200]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.670, canvas["w"] * 0.615],
                    "loc_y": [canvas["h"] * 0.025, canvas["h"] * 0.165, canvas["h"] * 0.305]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.425]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.300, canvas["h"] * 0.550]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.175, canvas["h"] * 0.425, canvas["h"] * 0.675]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.350]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.225, canvas["h"] * 0.475]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.725, canvas["w"] * 0.725, canvas["w"] * 0.725],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.350, canvas["h"] * 0.600]
                }
            }
        }
    },
    "saltire": {
        "field": {
            "banner": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.750],
                    "loc_y": [canvas["h"] * 0.355, canvas["h"] * 0.355]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.750, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.355, canvas["h"] * 0.355, canvas["h"] * 0.050]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.750],
                    "loc_y": [canvas["h"] * 0.355, canvas["h"] * 0.355]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.750, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.355, canvas["h"] * 0.355, canvas["h"] * 0.700]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050, canvas["h"] * 0.550]
                },
                3: {
                    "size": charge_size["xs"],
                    "loc_x": [canvas["w"] * 0.425, canvas["w"] * 0.425, canvas["w"] * 0.425],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.525, canvas["h"] * 0.700]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.040]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.040, canvas["h"] * 0.740]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.750, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.425, canvas["h"] * 0.425, canvas["h"] * 0.075]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.050]
                },
                2: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.750],
                    "loc_y": [canvas["h"] * 0.355, canvas["h"] * 0.355]
                },
                3: {
                    "size": charge_size["s"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.750, canvas["w"] * 0.400],
                    "loc_y": [canvas["h"] * 0.355, canvas["h"] * 0.355, canvas["h"] * 0.700]
                }
            }
        },
    },
    "per bend": {
        "base": {
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
        "chief": {
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
        "chief": {
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
        "base": {
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
    },
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
    },
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
    },
    "per nothing": {
        "field": {
            "banner": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.250]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.050, canvas["w"] * 0.550],
                    "loc_y": [canvas["h"] * 0.250, canvas["h"] * 0.250]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.600, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.475, canvas["h"] * 0.475, canvas["h"] * 0.200]
                }
            },
            "heater": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.350]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.600, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.200, canvas["h"] * 0.550]
                }
            },
            "pennant": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.200]
                },
                2: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.350, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.400]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.180, canvas["w"] * 0.350, canvas["w"] * 0.520],
                    "loc_y": [canvas["h"] * 0.100, canvas["h"] * 0.350, canvas["h"] * 0.100]
                }
            },
            "rect": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.340]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.170, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.120, canvas["w"] * 0.580, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.220, canvas["h"] * 0.220, canvas["h"] * 0.570]
                }
            },
            "shield": {
                1: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.300]
                },
                2: {
                    "size": charge_size["l"],
                    "loc_x": [canvas["w"] * 0.300, canvas["w"] * 0.300],
                    "loc_y": [canvas["h"] * 0.125, canvas["h"] * 0.525]
                },
                3: {
                    "size": charge_size["m"],
                    "loc_x": [canvas["w"] * 0.100, canvas["w"] * 0.600, canvas["w"] * 0.350],
                    "loc_y": [canvas["h"] * 0.200, canvas["h"] * 0.200, canvas["h"] * 0.550]
                }
            }
        },
    },
}
