# main.py
from presets import assembled_views
from rendering._util_images import supply_guid, delete_all_images
from rendering.assembler import make_assembled_image
from rendering.charger import make_charge_image
from rendering.compositor import make_parted_image
from rendering.trimmer import make_trimmed_image


def main():
    # delete_all_images()
    #
    # configure_cairo()
    # surf1 = draw_field("g", "label", "o", 3)
    # sg = supply_guid()
    # surf1.write_to_png("rendering/img/" + sg + ".png")
    #
    # surf2 = draw_field("o", "blank", "s")
    # sg = supply_guid()
    # surf2.write_to_png("rendering/img/" + sg + ".png")
    #
    # print(sg)
    # delete_image_guid(sg)

    #compose_per_fess(surf1, surf2)

    delete_all_images()

    #make_charge_image({"tincture": "n"})
    assembled_views.make_default_test_data("")
    make_assembled_image(assembled_views.default_view)

    # pipeline1a = {"tincture": "g", "charge": "label", "quantity": 3, "charge-tincture": "o"}
    # pipeline1b = {"tincture": "a"}
    # pipeline2 = {"party": "per fess", "chief": pipeline1a, "base": pipeline1b}
    # pipeline3 = {"shape": "pennant", "field": pipeline2}
    #
    # make_charge_image(pipeline1a)
    # make_charge_image(pipeline1b)
    # make_parted_image(pipeline2)
    # make_trimmed_image(pipeline3)


main()
