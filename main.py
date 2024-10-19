import json
from pathlib import Path

from language._parser import CalcParser
from tatsu.util import asjson


def main():
    grammar_path = Path.joinpath(Path.cwd(), 'language', 'blazon.ebnf')
    code_path = Path.joinpath(Path.cwd(), 'language', 'test', 'sample.blzn')

    parser = CalcParser()
    ast = parser.parse(get_file_as_string(code_path), start='start')
    print(ast)
    print(json.dumps(asjson(ast), indent=2))


def get_file_as_string(file_path):
    file = open(file_path, 'r')
    data = file.read()
    return data


main()