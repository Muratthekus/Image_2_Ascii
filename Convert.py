import sys, time
from builtins import print

import keyboard
from PIL import Image, ImageDraw, ImageFont


class convert:
    def __init__(self, PATH):
        self.PATH = PATH
        self.image = Image.open(PATH)
        self.pix = self.image.load()
        self.char_map = self.char_map_uret()  # Karakter map'ini tutuyor

        self.gray_image = Image.new(self.image.mode,
                                    self.image.size)  # Orjinal resmin gray value'sine göre yeniden yazılması
        self.gray_image = self.gray_image_process()
        self.gray_image.save("gray.jpg")

    def char_map_uret(self):
        # Siyah-beyaz alb-an oranlarına göre sıralı karakterler
        liste = list("""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """)
        char = dict()
        for i in range(len(liste)):
            char[i] = liste[i]
        return char

    def gray_image_process(self):
        return self.image.convert('L')

    def ascii_converter(self):
        file = open("asci.txt", "w",)
        self.gray_image = Image.open("gray.jpg")
        self.gray_pix = self.gray_image.load()
        width, height = self.gray_image.size
        for i in range(0,width,5):
            for j in range(0,height,2):
                ascii_value = self.char_map.get(int((self.gray_pix[i, j] / 255) * 69))
                file.write(ascii_value)
            file.write("\n")

    def run(self):
        self.ascii_converter()
