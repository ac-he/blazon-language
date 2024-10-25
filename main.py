from pathlib import Path

from language.blazon_list import BlazonList
from rendering._image_management import delete_all_images


def main():
    delete_all_images()

    code_path = Path.joinpath(Path.cwd(), 'language', 'test', 'documentation.blzn')
    b = BlazonList(code_path)
    b.interpret_as_pseudocode()
    b.interpret_as_image()


main()
