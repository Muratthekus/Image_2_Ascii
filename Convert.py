from PIL import Image, ImageDraw, ImageFont
import os

desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")

def runner(PATH):
    PATH = PATH
    image = Image.open(PATH)
    char_map = char_map_func()  # Keep ascii character in a list
    gray_image = gray_image_process(image)
    gray_image.save("gray.jpg")
    ascii_converter(char_map)


def char_map_func():
    # <----darkest---------------------brightest-------------->
    liste = list("""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """)
    char = dict()
    for i in range(len(liste)):
        char[i] = liste[i]
    return char


def gray_image_process(image):
    return image.convert('L')


def ascii_converter(char_map):
    gray_image = Image.open("gray.jpg")
    gray_pix = gray_image.load()
    width, height = gray_image.size

    im = Image.new("RGB", gray_image.size, color="white")  # ascii character will write on this image
    font = ImageFont.truetype("arial.ttf", 3)
    drawer = ImageDraw.Draw(im)

    for i in range(0, width, 5):
        for j in range(0, height, 2):
            ascii_value = char_map.get(int((gray_pix[i, j] / 255) * 69))
            drawer.text((i, j), ascii_value, font=font, fill=(0, 0, 0))

    im.save(desktop+r"\ascii.png")
    print("Image saved your desktop")


if __name__ == "__main__":
    print("Please copy the image to your desktop")
    runner(PATH=desktop+"\\"+input("Please write filename(ex: image.png)"))
