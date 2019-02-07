import numpy as np
import sys, time
import keyboard
from PIL import Image, ImageDraw, ImageFont
from Convert import convert
from sys import argv

Convert = convert(r"C:\Users\murat\PycharmProjects\Snake\octocat.png")
Convert.run()