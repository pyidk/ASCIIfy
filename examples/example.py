import sys
sys.path.append(".\\..\\")

from ascii_art import ASCIIArt

image = ASCIIArt("./mona-lisa.jpg", path_to_font="./Helvetica-Bold-Font.ttf")
image.save("./mona-lisa_ascii.png")
