from PIL import Image, ImageDraw, ImageFont

WIDTH = 20
HEIGHT = 40

image = Image.new('RGB', (257*WIDTH, HEIGHT))

d1 = ImageDraw.Draw(image)

path = "UbuntuMono-R.ttf"

myFont = ImageFont.truetype(path, HEIGHT)

cnt = 0
for i in list(range(33,127)) + list(range(160, 257)):
    d1.text((i*WIDTH,0), chr(i), fill =(255, 255, 255),font=myFont)

image.save("characters.png")
