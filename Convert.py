import sys, time
import keyboard
from PIL import Image, ImageDraw, ImageFont


class convert:
    def __init__(self, PATH):
        self.PATH = PATH
        self.image = Image.open(PATH)
        self.pix = self.image.load()
        self.gray_image = Image.new(self.image.mode,self.image.size)  # Orjinal resmin gray value'sine göre yeniden yazılması
        self.gray_pix = self.gray_image.load()

    def char_map(self):
        # Siyah-beyaz alb-an oranlarına göre sıralı karakterler
        liste = list("""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """)
        char_map = dict()
        for i in range(len(liste)):
            char_map[i] = liste[i]
        return char_map

    def gray_image_process(self):
        RED, GREEN, BLUE = 0.299, 0.587, 0.114  # pixel'in gray value degerini bulmak icin carpacagımız katsayılar
        width, height = self.image.size
        for i in range(width):
            for j in range(height):
                gray_value = RED * self.pix[i, j][0] + GREEN * self.pix[i, j][1] + BLUE * self.pix[i, j][2]
                self.gray_pix[i, j] = (int(gray_value), int(gray_value), int(gray_value))

    def ascii_converter(self):
        ascii_image = Image.new(self.image.mode, self.image.size)
        pixel = ascii_image.load()
        width, height = self.image.size
        for i in range(width):
            for j in range(height):
                pixel[i, j] = (255, 255, 255)

        font = ImageFont.truetype("arial.ttf", 12)
        draw = ImageDraw.Draw(ascii_image)
        for i in range(width):
            if i % 100 == 0:
                print(i)
            for j in range(height):
                gray_value = self.gray_pix[i, j][0]
                char_value = self.char_map().get(int(gray_value / 255) * 69)
                draw.text((i, j), char_value, font=font, fill=(0, 0, 0))
        ascii_image.save("ascii.jpg")

    def write_image(self):
        pass

    def run(self):
        char_map = self.char_map()  # Karakter map'ini tutuyor
        self.gray_image_process()
        print("aa")
        self.ascii_converter()
