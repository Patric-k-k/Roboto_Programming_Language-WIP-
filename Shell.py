#Import Programming Language
import Roboto
from Roboto import bcolors as Colors
while True:
    text = input("$ ")
    result, error = Roboto.run("User", text)
    if error:
        print(Colors.FAIL + error.as_string() + Colors.ENDC)
    else:
        print(result)