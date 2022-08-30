#Import Programming Language
import Roboto
from Roboto import bcolors as Colors
while True:
    text = input("> ")
    result, error = Roboto.run("User", text)
    if text == 'exit':
        exit()
    else:
        if error:
            print(Colors.FAIL + error.as_string() + Colors.ENDC)
        else:
            parser = Roboto.Parser(result)
            parse_res = parser.basic_math()
            print(result)
