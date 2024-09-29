pre_flag_view = {
    "default_view": {
        "w": 3820,
        "h": 2100,
        "background": "bigmonitor-mid-grey.png",
        "crest-scale-width": 330,
        "override-shapes": False,
        "printboxes": [
            {
                "x": 100,
                "y": 100,
                "w": 3820 - (100 * 2),
                "h": 2100 - (100 * 2),
                "kerning": 30,
                "line-spacing": 40,
            }
        ],
        "print": {
            "output-directory": "default",
            "file-name-base": "default",
            "pdf": False,
            "include-timestamp": False,
            "clear-old-images": False
        }
    },
    "flagpoles": {
        "w": 1200,
        "h": 800,
        "background": "flagpoles-cartoon.png",
        "crest-scale-width": 180,
        "override-shapes": False,
        "printboxes": [
            {
                "x": 140,
                "y": 64,
                "w": 1200 - (140 * 2),
                "h": 800 - (64 * 2),
                "kerning": 64,
                "line-spacing": 127,
            }
        ],
        "overlay": "fabric",
        "print": {
            "output-directory": "default",
            "file-name-base": "flagpoles",
            "pdf": False,
            "include-timestamp": False,
            "clear-old-images": False
        }
    },
    "photorealistic": {
        "w": 1536,
        "h": 1200,
        "background": "papplewick.png",
        "crest-scale-width": 220,
        "kerning": 60,
        "line-spacing": 94.5,
        "override-shapes": False,
        "printboxes": [
            {
                "x": 90,
                "y": 58,
                "w": 1536 - (90 * 2),
                "h": 1200 - (58 * 2),
                "kerning": 60,
                "line-spacing": 94.5,
            }
        ],
        "shapes": [
            "rect"
        ],
        "overlay": "fabric",
        "print": {
            "output-directory": "default",
            "file-name-base": "photo",
            "pdf": False,
            "include-timestamp": False,
            "clear-old-images": False
        }
    },
    "armorial": {
        "w": 800,
        "h": 600,
        "background": "armorial-folio.png",
        "crest-scale-width": 95,
        "printboxes": [
            {
                "x": 55,
                "y": 60,
                "w": 340,
                "h": 500,
                "kerning": 10,
                "line-spacing": 50,
            },
            {
                "x": 450,
                "y": 65,
                "w": 340,
                "h": 500,
                "kerning": 10,
                "line-spacing": 50,
            }
        ],
        "override-shapes": True,
        "shapes": [
            "heater"
        ],
        "page-overlay": "armorial-folio",
        "print": {
            "output-directory": "default",
            "file-name-base": "Armorial-Folio",
            "pdf": False,
            "include-timestamp": False,
            "clear-old-images": False
        }
    },
}

