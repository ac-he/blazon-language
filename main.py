from pathlib import Path

from language.blazon import Blazon


def main():
    code_path = Path.joinpath(Path.cwd(), 'language', 'test', 'sample.blzn')
    b = Blazon(code_path)
    b.parse_file()


main()
