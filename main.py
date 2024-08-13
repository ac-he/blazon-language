from presets import assembled_views
from rendering.charger import make_charge_image
from rendering.compositor import make_parted_image
from rendering.trimmer import make_trimmed_image
from rendering.z_util_images import delete_all_images, configure_svg_assets
from rendering.assembler import make_assembled_image


def main():
    # DEMO: These are just setup tasks
    # configure_svg_assets()
    delete_all_images()

    mode = "div-set"

    # DEMO: This will generate test flags, primarily to demonstrate division of field and charge arrangements.
    #       I have been -- and plan to continue -- using this to see what needs to be fixed at a glance.
    #       If you run this, note that different shapes of flag/crest will have different fess points!
    #       PARAM charge... The charge to include on the flag. Currently, it accepts only an empty string for
    #           a blank element or "label" which creates a label shape, though it does not render correctly at
    #           present.
    #       PARAM quantity... The number of charges to include per division of the field. Counterintuitively and
    #           for at-a-glance debugging reasons, it does not print one set of flags with this quantity on all
    #           of them. Rather, this represents the number of sets of flags that will be printed, with the
    #           number of charges in each set incremented. Because of this, the number of flags printed is 40 times
    #           the specified quantity. This is untested for values exceeding 3, because I don't plan on ever having
    #           the value exceed 3 "in real life".
    if mode == "set":
        assembled_views.make_default_test_data(assembled_views.charges, 3)
        make_assembled_image(assembled_views.default_view)

    if mode == "div-set":
        assembled_views.make_default_test_data_by_division("per pale", assembled_views.charges, 3)
        make_assembled_image(assembled_views.default_view)

    # DEMO: The general rendering pipeline is:
    #       User Input =dict=> Assembler =dict=> Trimmer =dict=> Compositor =dict=> Charger ===\
    #                        Combine flags     Trim flags       Divide flags      Add charges  ||
    #                        on background      to shape        into fields        to fields   ||
    #          Display <=png== Assembler <=png== Trimmer <=png== Compositor <=png== Charger <==/
    #       Each layer peels off the relevant information of the dictionary and then passes the rest
    #       to the next. Images are created at each step and their IDs are passed up the stack to
    #       the higher layers, where they are consumed and deleted.
    #       Because of this, input can actually be specified and received at any level, as the
    #       following code demonstrates.

    # Charge Level
    # Supported Charges:
    #   ""/default (does nothing)
    #   "label" (supported is a really generous term for this one)
    # Supported tinctures:
    #   "r"     argent      silver
    #   "o"     or          gold
    #   "g"     gules       red
    #   "v"     vert        green
    #   "a"     azure       blue
    #   "s"     sable       black
    #   "p"     purpure     purple
    if mode == "pipeline":
        pipeline1a = {"tincture": "g", "charge": "label", "quantity": 3, "charge-tincture": "o"}
        pipeline1b = {"tincture": "a"}
        print(f"Image 1a: {make_charge_image(pipeline1a)}")
        print(f"Image 1b: {make_charge_image(pipeline1b)}")

    # Compositor Level (Division of Field)
    # Supported Divisions:
    # "per bend"            dexter-base, sinister-chief
    # "per bend sinister"   sinister-base, dexter-chief
    # "per chevron"         chief, base
    # "per cross"           dexter-base, sinister-base, sinister-chief, dexter-chief
    # "per fess"            chief, base
    # "per pale"            dexter, sinister
    # "per pall"            dexter, sinister, chief
    # "per saltire"         dexter, sinister, chief, base
        pipeline2a = {"party": "per fess", "chief": pipeline1a, "base": pipeline1b}
        pipeline2b = {"party": "per pale", "dexter": pipeline1a, "sinister": pipeline1b}
        print(f"Image 2a: {make_parted_image(pipeline2a)}")
        print(f"Image 2b: {make_parted_image(pipeline2b)}")

    # Trimmer Level
    # Supported Shapes:
    # "banner"
    # "heater"
    # "pennant"
    # "rect"
    # "shield"
        pipeline3a = {"shape": "heater", "field": pipeline2a}
        pipeline3b = {"shape": "banner", "field": pipeline2b}
        print(f"Image 3a: {make_trimmed_image(pipeline3a)}")
        print(f"Image 3b: {make_trimmed_image(pipeline3b)}")

    # In the future the Assembler will also have options, such as the ability to override flag shapes (to
    # randomize them, etc), change the background so that it looks like they're all hung up outdoors or in
    # front of a stone or wooden wall, specify a path and format to save to (pdf?) and determine the spacing.
    # Some of those features already exist to an extent in assembled_views.py but the implementation is
    # nonexistent or broken for some of them.

    if mode == "single":
        pipeline1a = {"shape": "pennant", "field": {"party": "per pale",
                      "dexter": {"tincture": "v", "charge": "castle", "quantity": 3},
                      "sinister": {"tincture": "a", "charge": "sun"}
                      }}
        print(f"Image 1a: {make_trimmed_image(pipeline1a)}")


main()
