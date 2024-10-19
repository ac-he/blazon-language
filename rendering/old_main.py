import const
from presets.preset_flag_collections import pre_flag_collection
from presets.preset_flag_views import pre_flag_view
from presets.view_data_generator import make_randomized_test_data, make_default_test_data, \
    make_default_test_data_by_division
from rendering.charger import make_charge_image
from rendering.compositor import make_parted_image
from rendering.trimmer import make_trimmed_image
from rendering.assembler import make_assembled_image, draw_single_flag_with_overlay
from rendering.z_util_images import delete_all_images


def main():
    # DEMO: These are just setup tasks
    # configure_svg_assets()  # This will clear and re-create the sized versions of all the charges.
    delete_all_images()  # This removes previously generated images from rendering/img.

    # DEMO: PRESET MODES
    # "nice-renders"    Curated flag collections to show off the nice stuff this renderer can make.
    # "random"          A set of 40 random flags that show off the ugly stuff this renderer can make. These won't always
    #                   be pretty, but it's a good way to get a feel for what's all here.
    # "set"             Demonstrates what a charge looks like for all quantities, divisions, and shapes.
    #                   Mostly used when fine-tuning the values in const.py.
    # "div-set"         Demonstrates what a charge looks like for all quantities and shapes.
    #                   Mostly used when fine-tuning the values in const.py.
    # "pipeline"        Shows the steps of the process, largely for demo purposes. It should be the same as the previous
    #                   release.
    # "single"          Creates just one image, largely for demo purposes. It should be the same as last time.
    mode = "nice-renders"

    # NICE RENDERS
    if mode == "nice-renders":
        # NATO
        # This is specifying the background/assembly settings, stored in presets/preset_flag_views.py.
        collection_settings = pre_flag_view["default_view"]
        # You can specify where you'd like files to be output to.
        collection_settings["print"]["output-directory"] = "default"  # Change this to a filepath to save images to
        collection_settings["print"]["file-name-base"] = "default"  # Change this to a string to be the base filename
        collection_settings["print"]["include-timestamp"] = False  # Change this to true to add the time to the filename
                                                                   # (Pairs well with delete_all_images() disabled so
        #                                                          # they won't overwrite each other.)
        # This is adding the flag collection, pre-made and stored in presets/preset_flag_collections.py.
        collection_settings["crests"] = pre_flag_collection['nato']
        # Generate the image
        make_assembled_image(collection_settings)

        # FANTASY
        # Follows the same principles as above
        collection_settings = pre_flag_view["flagpoles"]
        collection_settings["print"]["file-name-base"] = "fantasy-"
        collection_settings["crests"] = pre_flag_collection['fantasy']
        make_assembled_image(collection_settings)

        # RANDOMIZED PHOTO
        # Follows the same principles as above.
        # See RANDOM MODE for information on how the randomized test data parameters work.
        collection_settings = pre_flag_view["photorealistic"]
        collection_settings["crests"] = make_randomized_test_data(15, charge_list="all", division_list="all",
                                                                  shape_list="all", quantity_list="all",
                                                                  quantity_frequencies=[7, 2, 1])
        make_assembled_image(collection_settings)

        collection_settings = pre_flag_view["armorial"]
        collection_settings["crests"] = make_randomized_test_data(23, charge_list="all", division_list="all",
                                                                  shape_list="all", quantity_list="all",
                                                                  quantity_frequencies=[7, 2, 1])
        make_assembled_image(collection_settings)

        collection_settings = pre_flag_view["armorial"]
        collection_settings["print"]["file-name-base"] = "armorial-nato"
        collection_settings["crests"] = pre_flag_collection['nato']
        make_assembled_image(collection_settings)

        collection_settings = pre_flag_view["armorial"]
        collection_settings["print"]["file-name-base"] = "armorial-fantasy"
        collection_settings["crests"] = pre_flag_collection['fantasy']
        make_assembled_image(collection_settings)

    if mode == "armorial":
        collection_settings = pre_flag_view["armorial"]
        collection_settings["print"]["file-name-base"] = "armorial-coin-toss"
        collection_settings["crests"] = pre_flag_collection['coin toss']
        make_assembled_image(collection_settings)

    # RANDOM MODE
    # You can override the lists here
    if mode == "random":
        data = pre_flag_view["default_view"]
        # CHARGE LIST -- "all" or a list of charges
        cl = ["fusily", "gyronny", "lozengy", "chequy", "fret", "gorge", "none", "none", "none"]
        # DIVISION LIST -- "all" or a list of divisions
        dl = ["per fess escutcheon"]
        # SHAPE LIST -- "all" or a list of shapes
        sl = "all"  # ["heater", "shield"]
        # QUANTITY LIST -- "all" or a list of quantities
        ql = "all"  # [1, 3]
        # QUANTITY FREQUENCIES -- "equal" or a list of frequencies corresponding to the quantity list.
        # For example, a 70% chance of 1 charge, 20% chance of 2 charges, and 10% chance of 3 charges,
        # if ql = [1, 2, 3] or "all" and qf = [7, 2, 1].
        qf = [7, 2, 1]  # [7, 1] or "equal"
        data["crests"] = make_randomized_test_data(40, charge_list=cl, division_list=dl, shape_list=sl,
                                                   quantity_list=ql, quantity_frequencies=qf)
        make_assembled_image(data)

    # DEMO: This will generate test flags, primarily to demonstrate division of field and charge arrangements.
    #       If you run this, note that different shapes of flag/crest will have different fess points!
    #       PARAM charge... The charge to include on the flag. Can be left blank or set to any of the included charges,
    #           as listed in const.py.
    #       PARAM quantity... The number of charges to include per division of the field. Counterintuitively and
    #           for at-a-glance debugging reasons, it does not print one set of flags with this quantity on all
    #           of them. Rather, this represents the number of sets of flags that will be printed, with the
    #           number of charges in each set incremented. Because of this, the number of flags printed is 40 times
    #           the specified quantity. This is untested for values exceeding 3, because I don't plan on ever having
    #           the value exceed 3 "in real life".
    #       PARAM division... (div-set only) The division of field to limit the set to. Acceptable values are:
    #           "per bend"          "per bend sinister"         "per bend both"         "per chevron"
    #           "per cross"         "per fess"                  "per pale"              "per pall"
    #           "per saltire"       "none"
    if mode == "set":
        data = pre_flag_view["default_view"]
        data["crests"] = make_default_test_data(["gyronny", "fret"], 1)
        make_assembled_image(data)

    if mode == "div-set":
        data = pre_flag_view["default_view"]
        data["crests"] = make_default_test_data_by_division("per fess escutcheon", ["label", "quarterly_of_eight"], 3)
        make_assembled_image(data)

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
    if mode == "pipeline":
        # Charge Level
        # Supported Charges:
        #   ""/default (does nothing)
        #   See const.py for a list of all charges and their settings.
        #   Charge Tinctures -
        #       Charges of type "cm" will have the charge tincture set automatically.
        #       Charges of types "agoprsv", "geo", and "oversize" will need a charge tincture specified.
        #       The charge "quarterly_of_eight" takes a list of eight tinctures as its charge-tincture.
        #       All others just use the one-character tincture as their charge-tinctures.
        #   Quantities -
        #       Charges of type "agoprsv" and "cm" as well as the charge "label" can have a quantity 1, 2, or 3.
        #       Charges of type "oversize" as well as the charge "quarterly_of_eight" don't obey quantity input.
        # Supported tinctures:
        #   "r"     argent      silver
        #   "o"     or          gold
        #   "g"     gules       red
        #   "v"     vert        green
        #   "a"     azure       blue
        #   "s"     sable       black
        #   "p"     purpure     purple
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
        # "None"                field
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

    # DEMO: SINGLE IMAGE
    #   Generates a single image. This basically combines the above pipeline demonstration into one step.
    if mode == "single":
        pipeline1a = {"shape": "heater",
                      "field": {
                          "party": "none",
                          "field": {
                              "tincture": "r",
                              "charge": "mullet",
                              "charge-tincture": "s",
                              "quantity": 2
                          },
                        }
                      }
        name = "example1"
        folder = "variable_nine"
        # print(f"Image 1a: {make_trimmed_image(pipeline1a)}")
        draw_single_flag_with_overlay(pipeline1a, "fabric",
                                      f"C:\\Users\\annac\\Code\\blazon-docs\\blazon-docs\\assets\\{folder}\\{name}.png")
        # make_trimmed_image(pipeline1a)

    if mode == "single-gen":
        for tincture in const.tinctures:
            pipeline1a = {"shape": "heater",
                          "field": {
                              "party": "none",
                              "field": {
                                  "tincture": tincture
                              }
                            }
                          }
            # pipeline1a = {"shape": "heater",
            #               "field": {
            #                   "party": "none",
            #                   "field": {
            #                       "tincture": "g",
            #                       "charge-tincture": "o",
            #                       "charge": charge,
            #                       "quantity": 1
            #                   }
            #               }
            #               }
            print(f"Image 1a: {make_trimmed_image(pipeline1a)}")
            draw_single_flag_with_overlay(pipeline1a, "fabric",
                                          f"C:\\Users\\annac\\Code\\blazon-docs\\blazon-docs\\assets\\tincture_chart\\{tincture}.png")


main()
