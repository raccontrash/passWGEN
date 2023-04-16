import pyfiglet
from termcolor import colored
# >> termcolor = color obj
def ANGRYBOYSINC():
    # criar obj
    f = pyfiglet.Figlet(font = 'catwalk')
    # imprimir texto
    T = (colored(f.renderText("WGEN"), "red"))
    print(T)

#   print(pyfiglet.FigletFont.getFonts())