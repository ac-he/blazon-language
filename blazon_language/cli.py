from blazon_language.language.blazon_list import BlazonList

import click


@click.group()
def main():
    pass


@main.command()
@click.argument("file")
@click.option(
    "--output-config", "-c",
    default="default",
    help="Output configuration file. See docs for specification."
)
@click.option(
    "--output-destination", "-o",
    default="here",
    help="Output configuration file. See docs for specification."
)
@click.option("--pseudocode", is_flag=True, default=False, help="Print pseudocode.")
@click.option("--no-images", is_flag=True, default=True, help="Render images.")
@click.option("--no-program", is_flag=True, default=True, help="Run program.")
def run(file, output_config, output_destination, pseudocode, no_images, no_program):
    b = BlazonList(file, output_config)

    if output_destination != "here":
        b.settings.image.output_destination = output_destination
        b.settings.pseudocode.output_destination = output_destination

    if pseudocode:
        b.interpret_as_pseudocode()
        print()
        print()
    if no_program:
        b.interpret_as_program()
        print()
        print()
    if no_images:
        b.interpret_as_image()


@main.command()
@click.argument("file")
@click.option("--step-thru", "-s", is_flag=True, default=False,
              help="Step through debug statements individually.")
def debug(file, step_thru):
    b = BlazonList(file, "default")
    b.settings.program.debug = True
    b.settings.program.step_thru = step_thru
    b.interpret_as_program()


main()
