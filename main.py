from pathlib import Path

from language.blazon_list import BlazonList


def main():
    code_path = Path.joinpath(Path.cwd(), 'language', 'test', 'cointoss.blzn')
    b = BlazonList(code_path)
    b.interpret_as_pseudocode()


main()
