import sys
from pyfiglet import Figlet
import random
figlet = Figlet()
if len(sys.argv) == 1:
    user_input = input("Input:")
    figlet.setFont(font= random.choice(figlet.getFonts()))
    print(figlet.renderText(user_input))

elif (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2]  in figlet.getFonts():
    user_input = input("Input:")
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(user_input))

else:
    sys.exit("Invalid usage")
    